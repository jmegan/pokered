"""
PokéBots Image Generation Pipeline — Gemini Generation Engine

Core reusable module for all image generation. Sends reference images + prompts
to the Gemini API (nano banana2 model) and saves the output as PNG.

All asset types (sprites, logos, badges, portraits) go through generate_image().
"""

import logging
import time
from io import BytesIO
from pathlib import Path

from google import genai
from google.genai import types
from PIL import Image

from config import GEMINI_API_KEY, GEMINI_MODEL, GEMINI_API_DELAY

logger = logging.getLogger(__name__)

# Initialize Gemini client once (reused across calls)
_client: genai.Client | None = None


def get_client() -> genai.Client:
    global _client
    if _client is None:
        _client = genai.Client(api_key=GEMINI_API_KEY)
    return _client


def generate_image(
    prompt: str,
    output_path: Path,
    reference_image: Path | None = None,
    fallback_prompt: str | None = None,
    aspect_ratio: str = "1:1",
) -> Path | None:
    """
    Generate an image using Gemini (nano banana2) and save it as PNG.

    Args:
        prompt:          Text prompt describing the desired image
        output_path:     Where to save the generated PNG
        reference_image: Optional reference image to guide generation
        aspect_ratio:    Output aspect ratio (e.g., "1:1", "16:9")

    Returns:
        Path to the saved PNG, or None on failure.
    """
    if output_path.exists():
        logger.info(f"Already generated: {output_path.name} — skipping")
        return output_path

    client = get_client()
    contents: list = [prompt]

    if reference_image and reference_image.exists():
        ref_img = Image.open(reference_image)
        contents.append(ref_img)
        logger.info(f"Using reference image: {reference_image.name}")

    logger.info(f"Generating: {output_path.name}...")
    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=contents,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
            ),
        )
    except Exception as e:
        logger.error(f"Gemini API error for {output_path.name}: {e}")
        return None

    candidate = response.candidates[0] if response.candidates else None
    parts = (candidate.content.parts if candidate and candidate.content else None) or []
    for part in parts:
        if part.inline_data and part.inline_data.data:
            try:
                img = Image.open(BytesIO(part.inline_data.data))
                output_path.parent.mkdir(parents=True, exist_ok=True)
                img.save(output_path, "PNG")
                logger.info(f"Saved: {output_path.name}")
                return output_path
            except Exception as e:
                logger.error(f"Failed to save {output_path.name}: {e}")
                return None

    # If reference image was provided and got refused (copyright/safety), retry text-only
    if reference_image:
        retry_prompt = fallback_prompt if fallback_prompt else prompt
        logger.warning(
            f"No image data with reference for {output_path.name} — "
            "likely copyright/safety block. Retrying text-only..."
        )
        return generate_image(
            prompt=retry_prompt,
            output_path=output_path,
            reference_image=None,
        )

    logger.warning(f"No image data in Gemini response for {output_path.name}")
    return None


def generate_bot_sprites(
    slot_id: int,
    bot_name: str,
    type_1: str,
    type_archetype: str,
    display_notes: str,
    avatar_path: Path | None,
    front_out: Path,
    back_out: Path,
    delay: float = GEMINI_API_DELAY,
) -> dict[str, Path | None]:
    """
    Generate front and back sprites for a single bot.

    Returns:
        Dict with keys "front" and "back" → Path or None
    """
    from config import FRONT_SPRITE_PROMPT, BACK_SPRITE_PROMPT, FRONT_SPRITE_FALLBACK_PROMPT, GLITCHBOT_FRONT_PROMPT, GLITCHBOT_BACK_PROMPT

    results: dict[str, Path | None] = {"front": None, "back": None}

    # ── Front sprite ──────────────────────────────────────────────────────────
    if not front_out.exists():
        front_fallback_prompt = None
        if bot_name.upper() == "GLITCHBOT" or not avatar_path:
            front_prompt = GLITCHBOT_FRONT_PROMPT
            ref = None
        else:
            # Primary prompt assumes reference image is provided
            front_prompt = FRONT_SPRITE_PROMPT
            # Fallback prompt (used if reference blocked) describes character from display_notes
            visual_description = display_notes or f"A {type_1}-type character named {bot_name}"
            front_fallback_prompt = FRONT_SPRITE_FALLBACK_PROMPT.format(
                visual_description=visual_description
            )
            ref = avatar_path

        results["front"] = generate_image(
            prompt=front_prompt,
            output_path=front_out,
            reference_image=ref,
            fallback_prompt=front_fallback_prompt if ref else None,
        )
        time.sleep(delay)
    else:
        logger.info(f"[{slot_id:03d}] Front sprite already exists: {front_out.name}")
        results["front"] = front_out

    # ── Back sprite ───────────────────────────────────────────────────────────
    if not back_out.exists():
        if bot_name.upper() == "GLITCHBOT" or not avatar_path:
            back_prompt = GLITCHBOT_BACK_PROMPT
        else:
            back_prompt = BACK_SPRITE_PROMPT.format(
                front_description=(
                    f"A {type_1}-type Pokémon-like creature named {bot_name}. "
                    f"Personality: {display_notes or type_archetype}. "
                    f"Type archetype: {type_archetype}."
                )
            )

        # Use the generated front sprite as reference for the back view
        front_ref = front_out if front_out.exists() else None
        results["back"] = generate_image(
            prompt=back_prompt,
            output_path=back_out,
            reference_image=front_ref,
        )
        time.sleep(delay)
    else:
        logger.info(f"[{slot_id:03d}] Back sprite already exists: {back_out.name}")
        results["back"] = back_out

    return results
