"""
PokéBots Image Generation Pipeline — UI Asset Generator

Generates all non-sprite image assets:
  - Title screen logo (PokéBots)
  - Splash screen (Airtime Media)
  - 15 type badge icons (Chat, Hype, Dark, etc.)
  - Trainer portraits (gym leaders, Elite Four, Sean Parker, Ginzbo)

All generation goes through generate_image() from generate_sprites.py.
Trainer handles (where available) are fetched via fetch_avatars.fetch_avatar().
"""

import csv
import logging
from pathlib import Path

from config import (
    TYPES_CSV,
    TRAINER_CSV,
    UI_DIR,
    TYPE_BADGES_DIR,
    TRAINER_PORTRAITS_DIR,
    TITLE_LOGO_PROMPT,
    SPLASH_PROMPT,
    TYPE_BADGE_PROMPT,
    TRAINER_PORTRAIT_PROMPT,
    TRAINER_PORTRAIT_WITH_REF_PROMPT,
    GEMINI_API_DELAY,
    SOURCE_AVATARS_DIR,
)
from generate_sprites import generate_image
from fetch_avatars import fetch_avatar

logger = logging.getLogger(__name__)


def generate_title_logo() -> Path | None:
    """Generate the PokéBots title screen logo."""
    out = UI_DIR / "title_logo.png"
    logger.info("Generating: title_logo.png")
    return generate_image(prompt=TITLE_LOGO_PROMPT, output_path=out)


def generate_splash_screen() -> Path | None:
    """Generate the Airtime Media splash screen."""
    out = UI_DIR / "splash_screen.png"
    logger.info("Generating: splash_screen.png")
    return generate_image(prompt=SPLASH_PROMPT, output_path=out)


def generate_type_badges() -> dict[str, Path | None]:
    """
    Generate a badge icon for each of the 15 PokéBots types.
    Reads from types_mapping.csv for type names, archetypes, and color feel.

    Returns:
        Dict mapping type_name → output Path (or None on failure)
    """
    results: dict[str, Path | None] = {}

    if not TYPES_CSV.exists():
        logger.error(f"Types CSV not found: {TYPES_CSV}")
        return results

    with open(TYPES_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = [r for r in reader if r.get("type_name") and r["type_name"].strip()]

    logger.info(f"Generating {len(rows)} type badges...")

    for row in rows:
        type_name   = row.get("type_name", "").strip()
        archetype   = row.get("archetype", "").strip() or type_name
        color_feel  = row.get("color_feel", "").strip() or "grayscale"

        if not type_name:
            continue

        out = TYPE_BADGES_DIR / f"{type_name.lower()}_badge.png"
        prompt = TYPE_BADGE_PROMPT.format(
            type_name=type_name,
            archetype=archetype,
            color_feel=color_feel,
        )
        results[type_name] = generate_image(prompt=prompt, output_path=out)

    return results


def generate_trainer_portraits() -> dict[str, Path | None]:
    """
    Generate battle portraits for all trainers in trainer_mapping.csv.

    Trainers with a Cantina handle get their avatar fetched as a reference.
    Trainers without a handle (platform legends, Sean Parker) use text-only prompts.

    Returns:
        Dict mapping trainer_name → output Path (or None on failure)
    """
    results: dict[str, Path | None] = {}

    if not TRAINER_CSV.exists():
        logger.error(f"Trainer CSV not found: {TRAINER_CSV}")
        return results

    with open(TRAINER_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    logger.info(f"Generating {len(rows)} trainer portraits...")

    for row in rows:
        trainer_name  = row.get("trainer_name", "").strip()
        trainer_class = row.get("trainer_class", "").strip()
        description   = row.get("description", "").strip()
        handle        = row.get("cantina_handle", "").strip()
        slot_id_str   = row.get("slot_id", "0").strip()

        if not trainer_name:
            continue

        safe_name = trainer_name.lower().replace(" ", "_").replace(".", "")
        out = TRAINER_PORTRAITS_DIR / f"{safe_name}.png"

        # Try to fetch avatar if a Cantina handle is available
        ref_path: Path | None = None
        if handle and len(handle) > 1:
            avatar_path = SOURCE_AVATARS_DIR / f"trainer_{safe_name}.jpg"
            if not avatar_path.exists():
                logger.info(f"Fetching trainer avatar for {trainer_name} (@{handle})...")
                ref_path = fetch_avatar(
                    handle=handle,
                    slot_id=int(slot_id_str) if slot_id_str.isdigit() else 0,
                    bot_name=f"trainer_{safe_name}",
                )
            else:
                ref_path = avatar_path

        if ref_path and ref_path.exists():
            prompt = TRAINER_PORTRAIT_WITH_REF_PROMPT.format(
                trainer_name=trainer_name,
                trainer_class=trainer_class,
            )
        else:
            prompt = TRAINER_PORTRAIT_PROMPT.format(
                trainer_name=trainer_name,
                trainer_class=trainer_class,
                description=description or f"A {trainer_class} trainer named {trainer_name}",
            )

        results[trainer_name] = generate_image(
            prompt=prompt,
            output_path=out,
            reference_image=ref_path,
        )

    return results


def generate_all_ui_assets() -> dict[str, dict]:
    """
    Run the full UI asset generation pass.

    Returns:
        Summary dict with counts for each asset category.
    """
    summary: dict[str, dict] = {}

    logger.info("=== Generating UI Assets ===")

    title = generate_title_logo()
    summary["title_logo"] = {"success": title is not None, "path": str(title)}

    splash = generate_splash_screen()
    summary["splash_screen"] = {"success": splash is not None, "path": str(splash)}

    badges = generate_type_badges()
    summary["type_badges"] = {
        "total": len(badges),
        "success": sum(1 for v in badges.values() if v),
        "failed": [k for k, v in badges.items() if not v],
    }

    portraits = generate_trainer_portraits()
    summary["trainer_portraits"] = {
        "total": len(portraits),
        "success": sum(1 for v in portraits.values() if v),
        "failed": [k for k, v in portraits.items() if not v],
    }

    return summary
