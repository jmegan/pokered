"""
PokéBots Image Generation Pipeline — Batch Runner

Full end-to-end pipeline with progress tracking and resumability.

Usage:
  python batch_pipeline.py --mode sprites      # All 300 bot sprites
  python batch_pipeline.py --mode ui           # All UI assets
  python batch_pipeline.py --mode all          # Everything
  python batch_pipeline.py --slot 14           # Regenerate one specific slot
  python batch_pipeline.py --dry-run           # Preview what would run
  python batch_pipeline.py --mode avatars      # Only fetch source avatars (no generation)

Cost estimate: ~350 API calls total ≈ $10-15 at Gemini API rates
"""

import argparse
import csv
import json
import logging
import sys
import time
from pathlib import Path

from config import (
    SPECIES_CSV,
    SOURCE_AVATARS_DIR,
    SPRITES_FRONT_DIR,
    SPRITES_BACK_DIR,
    PROGRESS_FILE,
    MANIFEST_FILE,
    GAMEBOY_FRONT_SIZE,
    GAMEBOY_BACK_SIZE,
    GEMINI_API_DELAY,
)
from fetch_avatars import fetch_all_avatars, fetch_avatar
from generate_sprites import generate_bot_sprites
from generate_ui_assets import generate_all_ui_assets
from postprocess import postprocess_sprite

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

# ── Slots to skip (GLITCHBOT Easter eggs — no Cantina handle) ─────────────────
GLITCHBOT_SLOTS = {
    31, 32, 50, 52, 56, 61, 62, 63, 67, 68, 69, 79, 80, 81, 86, 87,
    94, 95, 115, 121, 122, 127, 134, 135, 137, 140, 146, 156, 159,
    160, 161, 162, 172, 174, 175, 181, 182, 183, 184,
}

# Suspicious handles that need manual verification
SKIP_HANDLES = {"", "h", "j"}


def load_species() -> list[dict]:
    """Load all bot rows from species_mapping.csv."""
    if not SPECIES_CSV.exists():
        logger.error(f"Species CSV not found: {SPECIES_CSV}")
        sys.exit(1)

    bots = []
    with open(SPECIES_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            slot_id = row.get("slot_id", "").strip()
            if not slot_id or not slot_id.isdigit():
                continue
            bots.append(row)

    logger.info(f"Loaded {len(bots)} species rows from CSV")
    return bots


def load_progress() -> dict:
    """Load progress tracking file (creates empty file if missing)."""
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {}


def save_progress(progress: dict) -> None:
    PROGRESS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


def save_manifest(manifest: dict) -> None:
    MANIFEST_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(MANIFEST_FILE, "w") as f:
        json.dump(manifest, f, indent=2)


def run_avatars(bots: list[dict], slot_filter: int | None, dry_run: bool) -> dict[int, Path]:
    """Download source avatars for all bots."""
    logger.info("=== Phase 1: Fetching Source Avatars ===")

    filtered = bots
    if slot_filter is not None:
        filtered = [b for b in bots if int(b["slot_id"]) == slot_filter]

    fetch_list = []
    for row in filtered:
        slot_id = int(row["slot_id"])
        # Handle is the first segment of display_notes before the first period
        # e.g. "stacys-mom. No evolution. Flirty bot..." → "stacys-mom"
        display_notes_raw = row.get("display_notes", "").strip()
        handle = display_notes_raw.split(".")[0].strip() if display_notes_raw else ""
        name = row.get("cantina_bot_name", row.get("bot_name", "BOT")).strip()

        if slot_id in GLITCHBOT_SLOTS:
            continue
        if handle in SKIP_HANDLES:
            logger.warning(f"[{slot_id:03d}] Skipping {name} — suspicious handle '{handle}'")
            continue

        # Extract handle from display_notes first segment before period
        notes_raw = row.get("display_notes", "").strip()
        handle = notes_raw.split(".")[0].strip() if notes_raw else ""
        fetch_list.append({
            "slot_id": slot_id,
            "bot_name": name.upper(),
            "handle": handle,
        })

    if dry_run:
        logger.info(f"[DRY RUN] Would fetch {len(fetch_list)} avatars")
        for item in fetch_list[:5]:
            logger.info(f"  [{item['slot_id']:03d}] {item['bot_name']} → cantina.com/users/{item['handle']}")
        if len(fetch_list) > 5:
            logger.info(f"  ... and {len(fetch_list) - 5} more")
        return {}

    return fetch_all_avatars(fetch_list)


def run_sprites(
    bots: list[dict],
    slot_filter: int | None,
    dry_run: bool,
    progress: dict,
    manifest: dict,
) -> None:
    """Generate front + back sprites for all bots, then post-process."""
    logger.info("=== Phase 2: Generating Bot Sprites ===")

    filtered = bots
    if slot_filter is not None:
        filtered = [b for b in bots if int(b["slot_id"]) == slot_filter]

    total = len(filtered)
    done  = 0

    for i, row in enumerate(filtered):
        slot_id   = int(row["slot_id"])
        name      = row.get("cantina_bot_name", "BOT").strip().upper()
        handle    = row.get("bot_id", row.get("handle", "")).strip()
        type_1    = row.get("type_1", "Chat").strip()
        notes     = row.get("display_notes", "").strip()

        # Look up type archetype from types_mapping if needed
        type_archetype = type_1  # fallback; batch can enrich this from types CSV

        # Build output paths
        front_raw  = SPRITES_FRONT_DIR / f"{slot_id:03d}_{name}_front_raw.png"
        back_raw   = SPRITES_BACK_DIR  / f"{slot_id:03d}_{name}_back_raw.png"
        front_out  = SPRITES_FRONT_DIR / f"{slot_id:03d}_{name}_front.png"
        back_out   = SPRITES_BACK_DIR  / f"{slot_id:03d}_{name}_back.png"

        slot_key = str(slot_id)
        prog = progress.get(slot_key, {})

        # Skip if fully done
        if prog.get("front") and prog.get("back") and slot_filter is None:
            logger.info(f"[{slot_id:03d}] {name} — already complete, skipping")
            done += 1
            continue

        if dry_run:
            is_glitch = slot_id in GLITCHBOT_SLOTS
            has_handle = handle not in SKIP_HANDLES and handle
            logger.info(
                f"[{slot_id:03d}] {name} | type={type_1} | "
                f"{'GLITCHBOT' if is_glitch else f'handle={handle}'} | "
                f"ref={'yes' if has_handle and not is_glitch else 'no'}"
            )
            continue

        # Resolve avatar path
        avatar_path: Path | None = None
        if slot_id not in GLITCHBOT_SLOTS and handle not in SKIP_HANDLES and handle:
            avatar_path = SOURCE_AVATARS_DIR / f"{slot_id:03d}_{name}.jpg"
            if not avatar_path.exists():
                logger.info(f"[{slot_id:03d}] Avatar not cached, fetching now...")
                avatar_path = fetch_avatar(handle, slot_id, name)
                time.sleep(0.5)

        # Generate raw sprites
        sprite_results = generate_bot_sprites(
            slot_id=slot_id,
            bot_name=name,
            type_1=type_1,
            type_archetype=type_archetype,
            display_notes=notes,
            avatar_path=avatar_path,
            front_out=front_raw,
            back_out=back_raw,
            delay=GEMINI_API_DELAY,
        )

        # Post-process: square-pad, resize, and save color + gray variants
        if sprite_results["front"] and front_raw.exists():
            color_out, gray_out = postprocess_sprite(front_raw, front_out, GAMEBOY_FRONT_SIZE)
            prog["front"] = str(color_out)
            prog["front_gray"] = str(gray_out)

        if sprite_results["back"] and back_raw.exists():
            color_out, gray_out = postprocess_sprite(back_raw, back_out, GAMEBOY_BACK_SIZE)
            prog["back"] = str(color_out)
            prog["back_gray"] = str(gray_out)

        # Update progress + manifest
        prog["avatar"] = str(avatar_path) if avatar_path else None
        progress[slot_key] = prog
        manifest[slot_key] = {
            "slot_id": slot_id,
            "bot_name": name,
            "front": str(front_out) if front_out.exists() else None,
            "back": str(back_out) if back_out.exists() else None,
            "source_avatar": str(avatar_path) if avatar_path else None,
        }

        done += 1
        save_progress(progress)
        save_manifest(manifest)

        logger.info(f"[{slot_id:03d}] {name} complete ({done}/{total})")

    if not dry_run:
        logger.info(f"Sprites complete: {done}/{total}")


def run_ui(dry_run: bool) -> None:
    """Generate all UI assets (logo, splash, type badges, trainer portraits)."""
    if dry_run:
        logger.info("[DRY RUN] Would generate: title_logo, splash_screen, 15 type badges, trainer portraits")
        return

    summary = generate_all_ui_assets()
    logger.info("UI Asset Generation Summary:")
    for category, info in summary.items():
        logger.info(f"  {category}: {info}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="PokéBots Image Generation Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--mode",
        choices=["sprites", "ui", "all", "avatars"],
        default="sprites",
        help="What to generate (default: sprites)",
    )
    parser.add_argument(
        "--slot",
        type=int,
        default=None,
        help="Only process a single species slot number (e.g. --slot 14)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would be generated without making API calls",
    )
    args = parser.parse_args()

    bots     = load_species()
    progress = load_progress()
    manifest: dict = {}

    if args.mode in ("sprites", "all", "avatars"):
        avatars = run_avatars(bots, args.slot, args.dry_run)
        if args.mode == "avatars":
            logger.info(f"Avatar-only mode done. Downloaded {len(avatars)} avatars.")
            return

    if args.mode in ("sprites", "all"):
        run_sprites(bots, args.slot, args.dry_run, progress, manifest)

    if args.mode in ("ui", "all"):
        run_ui(args.dry_run)

    if not args.dry_run:
        logger.info("Pipeline complete.")


if __name__ == "__main__":
    main()
