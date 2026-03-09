"""
Re-postprocess all existing raw sprites.

Regenerates both color and grayscale variants for every *_raw.png file found,
applying the latest postprocess logic (square-pad + dual output).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from config import SPRITES_FRONT_DIR, SPRITES_BACK_DIR, GAMEBOY_FRONT_SIZE, GAMEBOY_BACK_SIZE
from postprocess import postprocess_sprite

def reprocess_all():
    pairs = (
        [(p, p.parent / p.name.replace("_raw", ""), GAMEBOY_FRONT_SIZE)
         for p in SPRITES_FRONT_DIR.glob("*_front_raw.png")]
        +
        [(p, p.parent / p.name.replace("_raw", ""), GAMEBOY_BACK_SIZE)
         for p in SPRITES_BACK_DIR.glob("*_back_raw.png")]
    )
    print(f"Reprocessing {len(pairs)} sprites → color + gray variants each...")
    color_count = gray_count = 0
    for src, out, size in pairs:
        try:
            color_out, gray_out = postprocess_sprite(src, out, size)
            color_count += 1
            gray_count += 1
            print(f"  ✓ {color_out.name}  |  {gray_out.name}")
        except Exception as e:
            print(f"  ✗ {src.name}: {e}")
    print(f"\nDone. {color_count} color + {gray_count} gray variants written.")

if __name__ == "__main__":
    reprocess_all()
