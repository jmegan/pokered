"""
PokéBots Image Generation Pipeline — Post-Processor

Takes Gemini-generated PNG images (variable size/aspect ratio) and converts them to
Game Boy–compatible sizes: content crop, square-pad, nearest-neighbor resize.

Outputs TWO variants per sprite:
  - Color:     out path as-is  (e.g. 001_STACYSMOM_front.png)
  - Grayscale: stem + "_gray"  (e.g. 001_STACYSMOM_front_gray.png)
    4-tone quantized to match Game Boy palette constraints.

For .pic conversion (Game Boy compressed format), use the existing tools/gfx.c build tool.
"""

import logging
from pathlib import Path

from PIL import Image, ImageOps

logger = logging.getLogger(__name__)


def _crop_to_content(img: Image.Image) -> Image.Image:
    """Trim white/transparent padding by finding the bounding box of non-white content."""
    gray = img.convert("L")
    inverted = ImageOps.invert(gray)
    bbox = inverted.getbbox()
    if bbox:
        return img.crop(bbox)
    return img


def _pad_to_square(img: Image.Image) -> Image.Image:
    """
    Pad a non-square image to square with white background, centering the content.
    This ensures non-square Gemini outputs (e.g. 1424×748) resize correctly.
    """
    w, h = img.size
    if w == h:
        return img
    side = max(w, h)
    square = Image.new("RGBA", (side, side), (255, 255, 255, 255))
    offset_x = (side - w) // 2
    offset_y = (side - h) // 2
    square.paste(img, (offset_x, offset_y))
    return square


def postprocess_sprite(
    src: Path,
    out: Path,
    target_size: tuple[int, int],
    quantize_colors: int = 4,
) -> tuple[Path, Path]:
    """
    Resize a Gemini-generated sprite to Game Boy dimensions and save both variants.

    Args:
        src:             Source PNG from Gemini (variable size/aspect ratio)
        out:             Output path for the color PNG
        target_size:     Target (width, height) in pixels, e.g. (56, 56)
        quantize_colors: Number of grayscale tones for the gray variant (4 = Game Boy)

    Returns:
        Tuple of (color_path, gray_path).
    """
    img = Image.open(src).convert("RGBA")

    # 1. Trim white padding
    img = _crop_to_content(img)

    # 2. Pad to square so resize doesn't distort non-square Gemini outputs
    img = _pad_to_square(img)

    # 3. Resize with nearest-neighbor (preserves pixel art edges)
    img = img.resize(target_size, Image.NEAREST).convert("RGB")

    out.parent.mkdir(parents=True, exist_ok=True)

    # --- Color variant ---
    img.save(out, "PNG")
    logger.info(f"Postprocessed: {src.name} → {out.name} ({target_size[0]}x{target_size[1]}, color)")

    # --- Grayscale variant (4-tone quantized) ---
    gray_out = out.with_stem(out.stem + "_gray")
    gray = img.convert("L").quantize(colors=quantize_colors).convert("L")
    gray.save(gray_out, "PNG")
    logger.info(f"Postprocessed: {src.name} → {gray_out.name} ({target_size[0]}x{target_size[1]}, gray)")

    return out, gray_out


def postprocess_batch(
    pairs: list[tuple[Path, Path, tuple[int, int]]],
    quantize_colors: int = 4,
) -> list[Path]:
    """
    Post-process a batch of (src, out, target_size) tuples.

    Returns:
        List of successfully written color output paths.
    """
    outputs: list[Path] = []
    for src, out, size in pairs:
        try:
            color_out, _ = postprocess_sprite(src, out, size, quantize_colors)
            outputs.append(color_out)
        except Exception as e:
            logger.error(f"Failed to postprocess {src.name}: {e}")
    return outputs
