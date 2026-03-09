# PokéBots Generated Image Assets

**Created:** 2026-03-08
**Last Updated:** 2026-03-08

This directory holds all generated image assets for the PokéBots reskin.

## Structure

```
images/
├── source_avatars/           # Downloaded Cantina bot avatars (og:image JPEGs, 1440x1440)
│   └── {slot_id}_{bot_name}.jpg
├── generated/
│   ├── sprites/
│   │   ├── front/            # Front battle sprites (56x56 PNG, 4-tone grayscale)
│   │   └── back/             # Back battle sprites (48x48 PNG, 4-tone grayscale)
│   ├── ui/
│   │   ├── title_logo.png    # PokéBots title screen logo
│   │   ├── splash_screen.png # Airtime Media splash
│   │   ├── type_badges/      # 15 type badge icons (32x32 PNG)
│   │   └── trainer_portraits/ # Gym leaders, Elite Four, Sean Parker (56x56 PNG)
│   └── manifest.json         # Maps slot_id → generated file paths
└── progress.json             # Pipeline progress tracker (resumable)
```

## Running the Pipeline

```bash
cd scripts/image_pipeline
pip install -r requirements.txt

# Create .env with your Gemini API key
echo "GEMINI_API_KEY=your_key_here" > ../../.env

# Smoke test (3 bots)
python batch_pipeline.py --slot 1 && python batch_pipeline.py --slot 14 && python batch_pipeline.py --slot 28

# Full bot sprites (~$9 in API costs)
python batch_pipeline.py --mode sprites

# UI assets (logo, splash, badges, portraits)
python batch_pipeline.py --mode ui

# Everything
python batch_pipeline.py --mode all

# Preview without API calls
python batch_pipeline.py --mode all --dry-run
```

## Converting to Game Boy Format

The PNG files here are intermediates for visual review. To convert to the Game Boy
`.pic` compressed format for use in the actual game build, use the existing build tool:

```bash
cd /path/to/Pokemon_Cantina
# The gfx.c tool handles PNG → .pic conversion as part of make
make
```

## Asset Counts

| Type | Count | Size |
|------|-------|------|
| Source avatars | ~150 | 1440×1440 JPEG |
| Front sprites | 150 (+ 39 GLITCHBOT) | 56×56 PNG |
| Back sprites | 150 (+ 39 GLITCHBOT) | 48×48 PNG |
| Type badges | 15 | 32×32 PNG |
| Trainer portraits | ~20 | 56×56 PNG |
| Title logo | 1 | 160×144 PNG |
| Splash screen | 1 | 160×144 PNG |

**Total API calls:** ~350 · **Estimated cost:** $10–15

## Notes

- GLITCHBOT slots (39 total) have no Cantina handle — generated from glitch archetype prompt only
- Slots 166 (HAWK) and 167 (JDVANCE) have suspicious single-char handles — skipped, need manual review
- All PNGs are generated at full quality and quantized to 4-tone grayscale post-generation
- The `progress.json` file lets you resume a partial run without re-generating completed slots
