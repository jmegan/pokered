"""
PokéBots Image Generation Pipeline — Configuration
All paths, model settings, style presets, and prompt templates live here.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from the Pokemon_Cantina project root
PROJECT_ROOT = Path(__file__).parent.parent.parent
load_dotenv(PROJECT_ROOT / ".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY or GEMINI_API_KEY == "your_key_here":
    raise EnvironmentError(
        "GEMINI_API_KEY not set. Create a .env file at:\n"
        f"  {PROJECT_ROOT / '.env'}\n"
        "with the line: GEMINI_API_KEY=your_actual_key\n"
        "Get a key at: https://aistudio.google.com/apikey"
    )

# ── Gemini model ──────────────────────────────────────────────────────────────
# "nano banana2" = gemini-2.0-flash-preview-image-generation
# Confirm latest model ID at: https://ai.google.dev/gemini-api/docs/image-generation
GEMINI_MODEL = "gemini-3.1-flash-image-preview"  # nano banana2

# ── Paths ─────────────────────────────────────────────────────────────────────
MAPPING_DIR     = PROJECT_ROOT / "docs" / "cantina" / "mapping"
SPECIES_CSV     = MAPPING_DIR / "species_mapping.csv"
TYPES_CSV       = MAPPING_DIR / "types_mapping.csv"
TRAINER_CSV     = MAPPING_DIR / "trainer_mapping.csv"

IMAGES_DIR          = PROJECT_ROOT / "images"
SOURCE_AVATARS_DIR  = IMAGES_DIR / "source_avatars"
GENERATED_DIR       = IMAGES_DIR / "generated"
SPRITES_FRONT_DIR   = GENERATED_DIR / "sprites" / "front"
SPRITES_BACK_DIR    = GENERATED_DIR / "sprites" / "back"
UI_DIR              = GENERATED_DIR / "ui"
TYPE_BADGES_DIR     = UI_DIR / "type_badges"
TRAINER_PORTRAITS_DIR = UI_DIR / "trainer_portraits"
PROGRESS_FILE       = IMAGES_DIR / "progress.json"
MANIFEST_FILE       = GENERATED_DIR / "manifest.json"

# ── Rate limiting ─────────────────────────────────────────────────────────────
AVATAR_FETCH_DELAY  = 0.5   # seconds between Cantina profile fetches
GEMINI_API_DELAY    = 2.0   # seconds between Gemini API calls

# ── Game Boy sprite dimensions ────────────────────────────────────────────────
GAMEBOY_FRONT_SIZE  = (56, 56)
GAMEBOY_BACK_SIZE   = (48, 48)
GAMEBOY_BADGE_SIZE  = (32, 32)
GAMEBOY_PORTRAIT_SIZE = (56, 56)
GAMEBOY_FULL_SCREEN = (160, 144)

# ── Cantina profile URL template ──────────────────────────────────────────────
CANTINA_PROFILE_URL = "https://cantina.com/users/{handle}"

# ── Prompt templates ──────────────────────────────────────────────────────────

FRONT_SPRITE_PROMPT = """\
You are a pixel artist creating original Game Boy sprite art.

Using the visual appearance in the reference image as your creative inspiration,
draw an original front-facing battle sprite in the style of Pokémon Red/Blue (1996 Game Boy).

The sprite should capture the character's look — their shape, outfit, expression, and vibe —
but rendered entirely as an original pixel art creation in the Gen 1 Pokémon sprite style.

Requirements:
- Pixel art style matching original Gen 1 Pokémon sprites (Game Boy, 1996)
- Preserve the character's natural colors subtly — keep the color palette limited but present
- Front-facing battle pose, centered in frame, facing the viewer
- Clean white background, no border or frame
- Full body visible, filling roughly 70% of a square canvas
- Drawn in the style of the original Game Freak sprite artists
"""

BACK_SPRITE_PROMPT = """\
You are a pixel artist creating original Game Boy sprite art.

The reference image shows the FRONT battle sprite of a character.
Draw the matching BACK sprite — the same character seen from behind.

Requirements:
- Same character and outfit as the front sprite, now viewed from the back
- Back-facing pose, as used in Gen 1 Pokémon battle scenes when the player sends out their bot
- Same pixel art style with the same subtle color palette as the front sprite
- Slightly smaller and less detailed than the front — consistent with original Game Boy sprites
- Clean white background, no border
"""

FRONT_SPRITE_FALLBACK_PROMPT = """\
Create a Pokémon Red/Blue Game Boy battle sprite for a character with these visual traits:
{visual_description}

Requirements:
- Pixel art style matching the original Gen 1 Pokémon sprites exactly (1996 Game Boy)
- Limited but present color palette with natural colors subtly preserved
- Front-facing battle pose, centered in frame, facing toward the player
- Clean white background, no border or frame
- Full body visible, sized to fill roughly 70% of a square canvas
- Style should feel like it was drawn by the original Game Freak sprite artists in 1996
- Do not reproduce any specific copyrighted character — create an original interpretation
"""

GLITCHBOT_FRONT_PROMPT = """\
You are a Pokémon Red/Blue sprite artist from 1996.

Design a front-facing GLITCH Pokémon battle sprite — like MissingNo. from the original games.

Requirements:
- Pixel art style consistent with Game Boy Pokémon Red/Blue (1996)
- 4-tone grayscale palette only (white, light gray, dark gray, black)
- The sprite should look corrupted, glitchy, fragmented — not a normal creature
- Inspired by MissingNo. but unique — blocky digital artifacts, scrambled pixels
- Battle-ready pose, centered in frame
- Clean white background
"""

GLITCHBOT_BACK_PROMPT = """\
Create the BACK sprite for a Glitch-type corrupted Pokémon (like MissingNo.).

Requirements:
- Same pixel art style and 4-tone grayscale palette
- Back-facing corrupted silhouette, smaller than front
- Digital artifacts and scrambled pixel pattern
- Clean white background
"""

TITLE_LOGO_PROMPT = """\
Design the title screen logo for a Game Boy game called 'PokéBots'.

Requirements:
- Pixel art style matching the Pokémon Red/Blue title screen logo (1996 Game Boy era)
- Bold, blocky lettering spelling exactly: PokéBots
- The text should have a drop shadow or outline for that classic Game Boy game title feel
- 4-tone grayscale palette (white, light gray, dark gray, black)
- Clean white background
- Wide horizontal composition (landscape orientation)
"""

SPLASH_PROMPT = """\
Design a studio splash screen logo for 'Airtime Media'.

Requirements:
- Pixel art style matching the classic Game Freak studio splash (shown at Game Boy game startup)
- Simple, clean logo mark + company name 'Airtime Media'
- Should feel like the bouncing Game Freak Pokémon logo but for a modern AI company
- 4-tone grayscale palette (white, light gray, dark gray, black)
- Clean white background
- Square or slightly horizontal composition
"""

TYPE_BADGE_PROMPT = """\
Design a small icon/badge for the '{type_name}' type in a Game Boy Pokémon-style battle UI.

Type personality archetype: {archetype}
Color mood: {color_feel}

Requirements:
- Pixel art style, Game Boy era (1996)
- Simple, iconic symbol — should be readable at 32x32 pixels
- 4-tone grayscale palette (white, light gray, dark gray, black)
- White background
- The icon should visually represent the {type_name} archetype
"""

TRAINER_PORTRAIT_PROMPT = """\
Design a trainer battle portrait in Game Boy Pokémon Red/Blue style.

Trainer name: {trainer_name}
Trainer class: {trainer_class}
Description: {description}

Requirements:
- Pixel art style consistent with Game Boy Pokémon Red/Blue trainer portraits (1996)
- Upper-body portrait, front-facing, centered
- 4-tone grayscale palette (white, light gray, dark gray, black)
- White background
- Style should match the 56x56 trainer battle sprites from the original games
"""

TRAINER_PORTRAIT_WITH_REF_PROMPT = """\
Design a trainer battle portrait in Game Boy Pokémon Red/Blue style.

Trainer name: {trainer_name}
Trainer class: {trainer_class}

Using the reference avatar as inspiration for this trainer's look and vibe,
create a pixelated Game Boy-era battle portrait.

Requirements:
- Pixel art style consistent with Game Boy Pokémon Red/Blue trainer portraits (1996)
- Upper-body portrait, front-facing, centered
- 4-tone grayscale palette (white, light gray, dark gray, black)
- White background
- Should resemble the reference but rendered as pixel art
"""

# ── Style presets (maps asset type → size + prompt) ───────────────────────────
STYLE_PRESETS = {
    "pokemon_front":    {"size": GAMEBOY_FRONT_SIZE,    "prompt_key": "FRONT_SPRITE_PROMPT"},
    "pokemon_back":     {"size": GAMEBOY_BACK_SIZE,     "prompt_key": "BACK_SPRITE_PROMPT"},
    "type_badge":       {"size": GAMEBOY_BADGE_SIZE,    "prompt_key": "TYPE_BADGE_PROMPT"},
    "trainer_portrait": {"size": GAMEBOY_PORTRAIT_SIZE, "prompt_key": "TRAINER_PORTRAIT_PROMPT"},
    "title_logo":       {"size": GAMEBOY_FULL_SCREEN,   "prompt_key": "TITLE_LOGO_PROMPT"},
    "splash_screen":    {"size": GAMEBOY_FULL_SCREEN,   "prompt_key": "SPLASH_PROMPT"},
    "onboarding":       {"size": GAMEBOY_FULL_SCREEN,   "prompt_key": "TITLE_LOGO_PROMPT"},
}
