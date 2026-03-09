"""
PokéBots Image Generation Pipeline — Avatar Fetcher

Scrapes the og:image from each bot's public Cantina profile page and downloads
the source avatar JPEG locally. These serve as reference images for Gemini generation.

URL pattern:  https://cantina.com/users/{handle}
og:image CDN: external.cdn.signal.is (JWT-signed, publicly accessible)
"""

import time
import logging
from pathlib import Path

import requests
from bs4 import BeautifulSoup

from config import (
    CANTINA_PROFILE_URL,
    SOURCE_AVATARS_DIR,
    AVATAR_FETCH_DELAY,
)

logger = logging.getLogger(__name__)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
}


def fetch_avatar(handle: str, slot_id: int, bot_name: str) -> Path | None:
    """
    Fetch the og:image from a Cantina bot profile page and save it locally.

    Args:
        handle:   Cantina username slug (e.g. "stacys-mom")
        slot_id:  Species slot number (1-190)
        bot_name: Short bot name (e.g. "STACYSMOM")

    Returns:
        Path to the downloaded image, or None on failure.
    """
    url = CANTINA_PROFILE_URL.format(handle=handle)
    out_path = SOURCE_AVATARS_DIR / f"{slot_id:03d}_{bot_name}.jpg"

    if out_path.exists():
        logger.info(f"[{slot_id:03d}] Already downloaded: {out_path.name}")
        return out_path

    logger.info(f"[{slot_id:03d}] Fetching profile: {url}")
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
    except requests.RequestException as e:
        logger.warning(f"[{slot_id:03d}] Failed to fetch profile page for '{handle}': {e}")
        return None

    soup = BeautifulSoup(resp.text, "html.parser")
    og_tag = soup.find("meta", property="og:image")
    if not og_tag or not og_tag.get("content"):
        logger.warning(f"[{slot_id:03d}] No og:image found for '{handle}'")
        return None

    image_url = og_tag["content"]
    logger.info(f"[{slot_id:03d}] Downloading avatar from CDN...")
    try:
        img_resp = requests.get(image_url, headers=HEADERS, timeout=30)
        img_resp.raise_for_status()
    except requests.RequestException as e:
        logger.warning(f"[{slot_id:03d}] Failed to download avatar image for '{handle}': {e}")
        return None

    SOURCE_AVATARS_DIR.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(img_resp.content)
    logger.info(f"[{slot_id:03d}] Saved: {out_path.name}")
    return out_path


def fetch_all_avatars(bots: list[dict], delay: float = AVATAR_FETCH_DELAY) -> dict[int, Path]:
    """
    Fetch avatars for a list of bots.

    Args:
        bots:  List of dicts with keys: slot_id, bot_name, handle
        delay: Seconds to wait between requests

    Returns:
        Dict mapping slot_id → downloaded Path (only successful fetches)
    """
    results: dict[int, Path] = {}
    skip_handles = {"", "h", "j"}  # suspicious single-char handles (slots 166-167)

    for i, bot in enumerate(bots):
        slot_id  = int(bot["slot_id"])
        bot_name = bot["bot_name"].upper().replace(" ", "")
        handle   = bot.get("handle", "").strip()

        if not handle or handle in skip_handles:
            logger.warning(f"[{slot_id:03d}] Skipping '{bot_name}' — suspicious/missing handle '{handle}'")
            continue

        already_cached = (SOURCE_AVATARS_DIR / f"{slot_id:03d}_{bot_name}.jpg").exists()
        path = fetch_avatar(handle, slot_id, bot_name)
        if path:
            results[slot_id] = path

        # Only rate-limit when we actually made a network request
        if not already_cached and i < len(bots) - 1:
            time.sleep(delay)

    logger.info(f"Avatar fetch complete: {len(results)}/{len(bots)} succeeded")
    return results
