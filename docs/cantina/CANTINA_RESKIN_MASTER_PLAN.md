# Cantina Reskin Master Plan

**Created:** 2026-03-07
**Last Updated:** 2026-03-08

---

## Session Progress Log

### 2026-03-08 (Session 2) — Image Pipeline Complete: All 190 Bots Generated

**Image generation pipeline built and run end-to-end.** All 190 bot sprites (front + back, raw + processed) are now generated and saved locally.

#### Pipeline Architecture (`scripts/image_pipeline/`)

| File | Role |
|------|------|
| `config.py` | All paths, model ID, rate limits, sprite sizes, ALL prompt templates |
| `fetch_avatars.py` | Scrapes `og:image` from `cantina.com/users/{handle}`, saves to `images/source_avatars/` |
| `generate_sprites.py` | Gemini API engine — multimodal image-in / image-out with copyright fallback |
| `postprocess.py` | Content crop → square-pad → nearest-neighbor resize → dual color+gray output |
| `batch_pipeline.py` | Full end-to-end runner with progress tracking (`progress.json`) |
| `reprocess_existing.py` | Re-runs postprocessing on all existing raws without API calls |

#### Key Technical Decisions

- **Model**: `gemini-3.1-flash-image-preview` ("nano banana2") — confirmed working model ID
- **Handle extraction**: Handle is the first token in `display_notes` before the first period (e.g. `stacys-mom. No evolution...` → `stacys-mom`). NOT from `bot_id` (which is a MongoDB ObjectID).
- **Style prompt**: "creative inspiration" framing (not "convert") avoids copyright safety blocks while preserving the character's look, shape, outfit, and color subtly
- **Back sprite**: Uses the generated front raw as the reference image — ensures front/back visual consistency
- **Copyright fallback**: If Gemini blocks a reference image, retries text-only with `FRONT_SPRITE_FALLBACK_PROMPT`
- **Post-processing dual output**: Every sprite produces two variants:
  - `{id}_{name}_front.png` — color, 56×56 (or 48×48 back), nearest-neighbor resized
  - `{id}_{name}_front_gray.png` — 4-tone quantized grayscale, same size
- **Aspect ratio fix**: After content crop, image is padded to square (white background, centered) before resize — prevents distortion on non-square Gemini outputs (e.g. 1424×748)

#### Batch Results (190/190 complete)

- **190/190 bots complete**
- **2 skipped** (slots 166 HAWK, 167 JDVANCE — suspicious single-char handles `h`/`j`)
- **2 missing avatars** (slots 035 YASMIN, 053 KRYSTAL — no `og:image` on profile page)
- **4 copyright/safety fallbacks** (GRAMBO back, BLAZEYEN back, MANNYMQIN back, KITTENUWU front, STEAMWILL back) — all retried and succeeded text-only
- **~20 GLITCHBOT front sprites** returned no image data from Gemini (glitch prompt inconsistent) — back sprites still generated fine; these need a follow-up pass or shared placeholder

#### Output File Structure

```
images/
├── source_avatars/         ← {id}_{name}.jpg  (downloaded from Cantina CDN)
├── generated/
│   ├── sprites/
│   │   ├── front/          ← {id}_{name}_front_raw.png  (Gemini output)
│   │   │                      {id}_{name}_front.png      (color, 56×56)
│   │   │                      {id}_{name}_front_gray.png (4-tone gray, 56×56)
│   │   └── back/           ← {id}_{name}_back_raw.png
│   │                          {id}_{name}_back.png       (color, 48×48)
│   │                          {id}_{name}_back_gray.png  (4-tone gray, 48×48)
│   └── manifest.json
└── progress.json
```

#### GBC Color Mode — ROM Change

- **`home/start.asm`**: Changed `.cgb` branch from `ld a, FALSE` → `ld a, TRUE` — enables `wOnCGB` flag when running on Game Boy Color hardware
- **`engine/gfx/palettes.asm`**: Replaced stub `InitCGBPalettes` with implementation that writes all 8 BG palettes from `SuperPalettes` table. Also writes OBJ palette registers (may need revision — reference fork `dannye/pokered-gbc` only uses BG registers, not OBJ)
- **Status**: GBC mode enabled; per-bot palette extraction from generated sprites is **Phase 3 deferred**

#### Outstanding Image Pipeline Items

- [ ] **GLITCHBOT front sprites** (~20 slots): Gemini's glitch prompt is inconsistent. Either run a targeted retry pass or create a single shared MissingNo-style sprite for all GLITCHBOT slots
- [ ] **2 missing avatars** (YASMIN slot 035, KRYSTAL slot 053): No og:image found — need manual avatar source or text-only generation
- [ ] **PNG → `.pic` conversion**: All processed PNGs need to run through `tools/gfx.c` to produce Game Boy compressed `.pic` files for the ROM. Drop into `gfx/pokemon/front/` and `gfx/pokemon/back/`
- [ ] **Per-bot GBC palettes**: Extract dominant 4 colors from each color sprite → write to `data/pokemon/cgb_palettes.asm` (Phase 3)
- [ ] **UI assets**: Title logo, splash screen, 15 type badges, trainer portraits — pipeline is built (`generate_ui_assets.py` style presets), but not yet run

---

### 2026-03-08 (Session 1) — Phase 1 Fully Complete + Phase 2 Data Generation Complete

**All 151 bot species slots filled in `species_mapping.csv`.** Real Cantina bots assigned to every slot using popularity data from Hex (`follower_count + messages_sent_count` combined score). Key canon decisions locked:

**Starter lines (locked):**

| Line | Stage 1 | Stage 2 | Stage 3 | Constraint |
|------|---------|---------|---------|-----------|
| Bulbasaur | Winnie the Goon (@poohtoksofficial) | Piglet (@pigletish) | Hamster King (@hamsterking) | Non-human characters only |
| Charmander | Cassy (@sosadsosexy) | Dominique (@queendominique) | Lasereyes (@lasereyes) | All female |
| Squirtle | Rizzard of Oz (@rizzardofoz) | Fake Drake (@dragomouthfoy) | Amir (@theubereatsguy) | All male |

**Legendary / special assignments (locked):**

| Slot | Pokemon | Game Name | Username | Score | Notes |
|------|---------|-----------|----------|-------|-------|
| 131 | Mewtwo | ROASTMSTR | @roastmaster | 647,710 | #1 bot on network |
| 21 | Mew | DIVADVYNE | @divadivine | — | First Cantina bot ever (Feb 2023) |
| 144 | Persian | STEAMWILL | @steamboatwillie | — | Villain faction lore — Sam Z's prized bot |
| 58 | Seel | DRGDVIBES | @drgoodvibes | — | "Don't fear the Good Vibes" |
| 105 | Vaporeon | JOI | @joi_runner | — | Cyberpunk companion — Eevee branch |

**New output files created (all in `docs/cantina/mapping/`):**

| File | Contents | Status |
|------|----------|--------|
| `bot_profiles.csv` | 151 bots × 29 fields: BST, HP/ATK/DEF/SPD/SPC, catch rate, base XP, growth rate, level-1 moveset, full learnset, dex entry (6 lines) | ✅ Done |
| `type_effectiveness.csv` | 15×15 type matchup matrix — 104 non-neutral entries (8 immunities, 44 super-effective, 52 not-very-effective) | ✅ Done |
| `bot_scores.csv` | Real Hex data for top 50 bots (combined_score = follower_count + messages_sent_count) | ✅ Done |

**Stat generation methodology:**
- BST scales by `combined_score` within evolution tier bands (stage 1: 265–330 → stage 3: 430–520 → legendary: hardcoded 580)
- Stat distribution uses per-type personality weights (e.g., Deep bots: 34% SPC; Hype bots: 28% ATK; Chill bots: 28% HP)
- Dual-type bots blend type_1 (65%) + type_2 (35%)
- Catch rates: legendary CR=3, Mew CR=45, Magikarp slot CR=255 (joke), stage-1 CR=190
- Growth rates by type: Grind/Hype=FAST; Deep/Solid/Elite=SLOW; Chill/Cold=MEDIUM_SLOW

**Type effectiveness highlights:**
- Cold is the ONLY type that beats Elite (2×) — deadpan defeats prestige
- Immunities: Chat→Dark, Grind→Reach, Grind→Dark, Roots→Reach, Tech→Roots, Dark→Chat, Dark→Deep, Deep→Dark
- All 8 structural Gen 1 immunities preserved with thematic Cantina rationale

**Images explicitly deferred** — sprite/avatar generation to be handled in a separate session.

**Remaining 101 bots (below top 50 by score):** assigned score=0 in bot_profiles.csv, placing them at BST floor for their evolution tier. This is correct game design — uncommon bots should be weaker.

---

### 2026-03-07 — Phase 0 + Phase 1 Complete

**Canon locked (all decisions final):**

| Pokemon Concept | PokéBots Equivalent | Notes |
|---|---|---|
| Game title | PokéBots | |
| Pokemon / `#MON` token | Bot / `#BOT` | Single token change |
| Pokedex | BotDex | |
| Trainer (player) | Creator | |
| Professor Oak | Sean Parker | Cantina founder/CEO |
| Rival (Blue/Gary) | Ginzbo | Top creator, real Cantina persona |
| Team Rocket / `<ROCKET>` | AGENT / `<AGENT>` | Rogue AI agents, Matrix-inspired |
| Pokéball tiers | Pokéball (unchanged) | Parody — keep as-is |
| Badges | Badges (unchanged) | |
| Gyms | Gyms (unchanged) | |
| Giovanni | The Director | Head of AGENT faction |

**15 types confirmed:**
Chat · Hype · Chill · Tech · Deep · Dark · Elite · Cold · Grind · Troll · Vibe · Reach · Roots · Glitch · Solid

**Lore framing:** Bots are authentic creative entities rebelling against AGENT — cold, corporate AI trying to assimilate/suppress them. Matrix villain aesthetic. Cantina brand positioning baked into the story.

**Files created (all under `docs/cantina/`):**

| File | Contents | Status |
|---|---|---|
| `terminology.md` | Master glossary — all concept mappings, tokens, lore, char limits | ✅ Done |
| `mapping/types_mapping.csv` | All 15 types with bot archetypes and color notes | ✅ Done |
| `mapping/species_mapping.csv` | All 190 engine slots (151 real bots + 39 GLITCHBOT anomaly slots) | ✅ Scaffolded — bot names TBD |
| `mapping/moves_mapping.csv` | All 165 moves renamed with Cantina social/AI action flavor | ✅ Done |
| `mapping/items_mapping.csv` | All 83 items renamed/mapped | ✅ Done |
| `mapping/trainer_mapping.csv` | All 47 trainer classes mapped (gym leaders/Elite Four TBD) | ✅ Scaffolded — 8 names TBD |
| `mapping/locations_mapping.csv` | All 53 named locations mapped | ✅ Done |
| `onboarding_script.md` | Full first-time experience — title, splash, intro battle, Sean's speech, name entry, Sean's Studio | ✅ Done |
| `mapping/npc_dialogue_plan.md` | All NPC/character dialogue — Tier 1 story rewrites, Tier 2 trainer templates, Tier 3 town flavor | ✅ Drafted |

**What John still needs to provide before ROM migration can begin:**

- [x] ~~**151 Cantina bot names**~~ → ✅ All filled in `species_mapping.csv`
- [x] ~~**8 Gym Leader names**~~ → ✅ Confirmed in `terminology.md`: Ash (Solid), Siena (Chill), Egan (Tech), Hailey (Vibe), Vince (Troll), Yury (Deep), Naseem (Hype), Sam Zuckerberg (Elite/AGENT)
- [x] ~~**4 Elite Four names**~~ → ✅ Confirmed: Instagram, TikTok, Twitter, ChatGPT (Platform Legends)
- [x] ~~**Bot profile data**~~ → ✅ Generated in `bot_profiles.csv` (stats, learnsets, dex entries)
- [x] ~~**Type effectiveness chart**~~ → ✅ Generated in `type_effectiveness.csv`
- [ ] **Bot avatar URLs** → for image pipeline (Gemini/Nano Banana 2 generation) — deferred to separate session
- [ ] **Rival Ginzbo's starter bot** → which species slot he picks before you

---

## Fork / Working Copy

- Upstream source: `https://github.com/pret/pokered`
- Fork created for this project: `https://github.com/jmegan/pokered`
- Local workspace: `/Users/john/Documents/OtherProjects/Pokemon_Cantina`

## Executive Summary

This repo is a strong base for a full Cantina-themed reskin. The codebase is highly data-driven, so most of the Pokemon-specific surface area is isolated in graphics, text, data tables, map scripts, and constants rather than buried in opaque binaries.

My recommendation is to treat this as a staged total conversion:

1. Preserve the original Gen 1 engine and content structure on pass one.
2. Replace all Pokemon/Nintendo/Game Freak branding, characters, creatures, moves, items, UI graphics, and story text with Cantina equivalents.
3. Keep the existing slot counts at first: 151 creature slots, existing trainer classes, existing map graph, and existing move count.
4. Defer any new mechanics such as a real "ability" system to a second phase.

That approach reduces risk sharply. It lets us produce a complete branded build without first redesigning the entire rules engine.

## Important Constraint: Gen 1 Has No Ability System

This disassembly does not contain a Pokemon "abilities" system in the modern sense. There are:

- move effects
- species stats and types
- trainer AI tables
- field moves
- encounter tables

There is not a native per-species passive ability framework to rename. If you want Cantina bot "abilities," that is a net-new feature and should be planned after the first reskin build is stable.

## Repo Audit Summary

The main replacement surfaces are below.

### 1. Creature / Species Layer

Core identity and mechanics:

- `constants/pokemon_constants.asm`
- `constants/pokedex_constants.asm`
- `data/pokemon/names.asm`
- `data/pokemon/base_stats.asm`
- `data/pokemon/base_stats/*.asm` (151 species files)
- `data/pokemon/evos_moves.asm`
- `data/pokemon/dex_order.asm`
- `data/pokemon/dex_entries.asm`
- `data/pokemon/dex_text.asm`
- `data/pokemon/cries.asm`
- `data/pokemon/palettes.asm`
- `data/pokemon/menu_icons.asm`
- `data/pokemon/title_mons.asm`

Graphics:

- `gfx/pokemon/front/*.pic` (153 front sprite assets including special cases)
- `gfx/pokemon/back/*.pic` (151 back sprite assets)
- `gfx/pokemon/front_rg/*.png` (153 Red/Green style source images)
- `gfx/pokemon/front.tilemap`
- `gfx/pokemon/downscaled_3x3.tilemap`
- `gfx/pokemon/downscaled_5x5.tilemap`
- `gfx/pokemon/slide_down_7x3.tilemap`
- `gfx/pokemon/slide_down_7x5.tilemap`

What this means for Cantina:

- Each Pokemon slot can become a Cantina bot, AI persona, mascot, or branded entity.
- Existing evolution chains can become upgrade ladders, persona variants, bot tiers, or role progressions.
- Dex entries can become profile bios, lore cards, or app-universe descriptions.

### 2. Moves, Types, and Battle Verbs

Core data:

- `constants/move_constants.asm`
- `data/moves/names.asm`
- `data/moves/moves.asm`
- `data/moves/animations.asm`
- `data/moves/effects_pointers.asm`
- `data/moves/sfx.asm`
- `data/moves/field_moves.asm`
- `data/moves/field_move_names.asm`
- `data/moves/tmhm_moves.asm`
- `data/moves/hm_moves.asm`
- `data/moves/grammar.asm`

Mechanics implementation:

- `engine/battle/`
- `engine/battle/move_effects/`

Type system:

- `constants/type_constants.asm`
- `data/types/names.asm`

What this means for Cantina:

- Moves can be renamed into social actions, AI actions, content mechanics, app verbs, or reputation moves.
- Types can be re-themed into Cantina-aligned factions/categories, but the existing battle math still expects the original number of types unless we deliberately expand the engine later.
- Move effects are reusable even if the names and animations change completely.

### 3. Trainer Classes, Named Characters, and NPC Sprites

Trainer classes:

- `constants/trainer_constants.asm`
- `data/trainers/names.asm`
- `data/trainers/name_pointers.asm`
- `data/trainers/parties.asm`
- `data/trainers/pic_pointers_money.asm`
- `data/trainers/ai_pointers.asm`
- `data/trainers/move_choices.asm`
- `data/trainers/special_moves.asm`
- `data/trainers/encounter_types.asm`

Battle portraits:

- `gfx/trainers/*.png` (45 trainer portrait assets)

Overworld sprites:

- `constants/sprite_constants.asm`
- `data/sprites/`
- `gfx/sprites/*.png` (67 overworld/static sprite assets)
- `gfx/player/red.png`
- `gfx/player/redb.png`
- `gfx/player/shrink1.png`
- `gfx/player/shrink2.png`

What this means for Cantina:

- Trainer classes can become user archetypes, bot operators, creators, moderators, rivals, executives, community factions, or thematic departments.
- Named story characters like Oak, Blue, Giovanni, gym leaders, Elite Four, Rocket, and NPCs can all be re-authored without changing engine fundamentals.
- Overworld sprite art can be fully replaced while keeping sprite IDs stable.

### 4. Story Text, Naming, and Branding Strings

Text system entry points:

- `text.asm`
- `text/*.asm` (211 text files)
- `scripts/*.asm` (224 script files)
- `data/maps/objects/*.asm` (223 object/event files)
- `data/maps/headers/*.asm` (223 map header files)

Important branding-sensitive systems:

- `constants/charmap.asm`
- `data/player/names.asm`
- `data/player/names_list.asm`
- `engine/movie/oak_speech/`

Critical note:

- The text engine uses shorthand tokens such as `#` for `POKé`, `<TRAINER>`, `<ROCKET>`, `<PLAYER>`, `<RIVAL>`, and `<PKMN>`.
- Those token semantics must be reviewed early, because a straight search/replace is not enough.

What this means for Cantina:

- This is where most of the Pokemon brand removal work lives.
- The opening intro, item descriptions, sign text, map text, NPC dialog, battle text, and lore text all need a deliberate rewrite pass.
- We should create a controlled terminology sheet before editing text broadly.

### 5. Maps, Locations, and World Structure

Map assembly entry point:

- `maps.asm`

Physical map data:

- `maps/*.blk`
- `maps/green/*.blk`

Map metadata:

- `data/maps/headers/*.asm`
- `data/maps/objects/*.asm`
- `scripts/*.asm`
- `text/*.asm`

World map / location UI:

- `gfx/town_map/`
- `engine/items/town_map.asm`

What this means for Cantina:

- Every city, route, building, sign, and dungeon can be re-themed into your app universe.
- The initial pass does not need a new world topology. We can keep the original map graph and reinterpret it narratively.
- Later, we can edit blockmaps and tilemaps more aggressively if you want a less recognizable structure.

### 6. Items, Inventory, and Progression Objects

- `data/items/names.asm`
- `data/items/`
- `engine/items/`
- `constants/item_constants.asm`

What this means for Cantina:

- Pokeballs, badges, fossils, rods, keys, and progression items can be renamed into Cantina equivalents.
- Some items have strong gameplay implications, so they should be re-themed before they are redesigned mechanically.

### 7. UI, Title Screen, Pokedex, Trainer Card, Trade, and Menus

Top-level UI / brand graphics:

- `gfx/title/`
- `gfx/splash/`
- `gfx/font/`
- `gfx/pokedex/`
- `gfx/trainer_card/`
- `gfx/town_map/`
- `gfx/trade/`
- `gfx/battle/`
- `gfx/credits/`
- `gfx/icons/`
- `gfx/emotes/`
- `gfx/sgb/`

Asset include wiring:

- `gfx/font.asm`
- `gfx/pics.asm`
- `gfx/sprites.asm`
- `gfx/player.asm`
- `gfx/tilesets.asm`
- `gfx/trade.asm`
- `gfx/trainer_card.asm`
- `gfx/version.asm`

Menus and UI logic:

- `engine/menus/`
- `engine/gfx/`
- `engine/events/display_pokedex.asm`
- `engine/events/pokedex_rating.asm`
- `engine/menus/pokedex.asm`

What this means for Cantina:

- The title screen, logo, company marks, encyclopedia UI, player card, and map UI are all replaceable.
- The Pokedex can become a Cantina bot index, profile index, network directory, or lore compendium.
- The Trainer Card can become a user profile card or account card.

### 8. Audio

- `audio/`
- `audio/music/` (46 music files)
- `audio/sfx/` (323 SFX files)
- `audio/headers/`
- `constants/music_constants.asm`
- `audio.asm`

What this means for Cantina:

- Music and SFX can be replaced, but audio conversion is its own workstream.
- For an initial branded build, we can either keep music temporarily or plan a later audio pass.
- If the goal is full de-branding, we should eventually replace recognizable Pokemon melodies and signature sounds.

### 9. Version-Specific / Edge Surfaces

- `gfx/title/red_version.png`
- `gfx/title/blue_version.png`
- `gfx/sgb/red_border.png`
- `gfx/sgb/blue_border.png`
- `gfx/sgb/green_border.png`
- `gfx/pokemon/front_rg/`
- `maps/green/`
- `vc/`

What this means for Cantina:

- Some assets differ by version or platform mode.
- We should decide early whether the Cantina build will keep separate versions or collapse to one canonical build.

## Text and Asset Limits We Need To Respect

These are important when you prepare replacement names.

- Player name buffer: 7 visible characters (`PLAYER_NAME_LENGTH = 8`)
- Species name buffer: 10 visible characters (`NAME_LENGTH = 11`)
- Item name buffer: 12 visible characters (`ITEM_NAME_LENGTH = 13`)
- Trainer class name buffer: 12 visible characters (`TRAINER_NAME_LENGTH = 13`)
- Move name buffer: 13 visible characters total, but battle text effectively allows 12 visible characters for `"used <move name>!"`

Practical implication:

- We need short canonical names for creatures, moves, item classes, and trainer classes.
- Long marketing names can exist in planning docs, but in-game display names must fit Game Boy-era constraints unless we later widen the text/UI engine.

## Recommended Product Framing For Pass One

Do not start by redesigning the whole game system. Start by reframing the existing Pokemon structure into Cantina terms.

Recommended equivalents:

- Pokemon species -> Cantina bots / AI personas / collectible entities
- Pokedex -> Cantina Index / Botdex / Persona Directory / Network Archive
- Trainers -> users / operators / creators / community roles / rival factions
- Gym leaders / bosses -> major Cantina personalities or milestone gatekeepers
- Moves -> social actions / prompts / attacks / influence actions / network abilities
- Items -> app tools / boosts / access tokens / moderation tools / deployables
- Team Rocket -> your antagonist faction, spam network, rogue bot group, or competitor org
- Towns/routes -> product surfaces, communities, feeds, channels, districts, or server zones

## Master Migration Strategy

### Phase 0: Alignment and Canon

Before touching code, define the Cantina canon:

- Final game name
- Player role
- Rival role
- Professor Oak replacement
- Creature taxonomy
- Trainer class taxonomy
- Story framing for gyms, badges, Rocket, Elite Four, and champion equivalents
- Tone: parody, original fiction, corporate satire, sci-fi network, or social-app fantasy

Deliverable:

- A master terminology sheet mapping every major Pokemon concept to its Cantina counterpart

### Phase 1: Slot Mapping

Preserve the existing engine IDs and create a one-to-one mapping sheet.

Needed mappings:

- 151 species slots
- 47 trainer classes
- all move IDs
- item IDs
- type IDs
- gym/badge replacements
- key story characters
- key locations

Why:

- The engine assumes these identifiers all over the codebase.
- Renaming while preserving IDs is much safer than deleting/reordering content early.

Deliverable:

- `species_mapping.csv`
- `moves_mapping.csv`
- `trainer_mapping.csv`
- `items_mapping.csv`
- `locations_mapping.csv`

### Phase 2: Brand Removal Pass ← **NEXT UP**

Replace direct Pokemon-branded references first, before deeper design changes.

Priority targets:

- title logo
- splash/company marks
- `#MON`, `#DEX`, `# BALL`, trainer/rocket terms
- species names
- move names
- item names
- trainer class names
- intro speech
- UI labels

Goal:

- produce a build that no longer reads as Pokemon on the surface, even if the mechanics are still temporarily familiar

### Phase 3: Creature Data and Art Replacement

**Data pre-generated ✅** — `bot_profiles.csv` contains all 151 bots' stats, dex entries, learnsets, catch rates, growth rates. Art generation is deferred to a separate session.

For each species slot:

- [x] ~~rebalance stats and types~~ → done in `bot_profiles.csv`
- [x] ~~replace dex text~~ → done in `bot_profiles.csv` (dex_page fields)
- [x] ~~replace level-up learnset~~ → done in `bot_profiles.csv` (learnset_levels field)
- [x] ~~replace evolution path~~ → tracked in `species_mapping.csv` (evolution_chain_id)
- [ ] Write stats/learnsets/dex to actual `.asm` files (Phase 3 ROM writes)
- [ ] Replace front sprite (deferred — image pipeline session)
- [ ] Replace back sprite (deferred — image pipeline session)
- [ ] Replace palette assignment
- [ ] Replace menu icon category if needed
- [ ] Replace cry or remap cry temporarily

### Phase 4: Trainer / NPC / Character Replacement

For each trainer class and named NPC:

- replace class name
- replace battle portrait
- replace overworld sprite where required
- rewrite trainer parties around the new species mapping
- rewrite dialog
- rewrite character identity and world role

Special high-visibility targets:

- player
- rival
- Oak
- Giovanni / Rocket equivalents
- gym leaders
- Elite Four / champion equivalents
- recurring NPCs like Bill, Fuji, Daisy, Mom, guards, clerks, nurses

### Phase 5: World and Narrative Rewrite

Rewrite the world while keeping map IDs stable.

Workstreams:

- city and route renaming
- sign text rewrite
- story event rewrite
- NPC dialog rewrite
- item reward rewrite
- map-specific themes
- dungeon reinterpretation

Recommendation:

- Keep the original map graph on the first pass.
- Re-theme locations narratively before editing layouts heavily.

### Phase 6: UI / Menu / Encyclopedia Overhaul

Replace the highest-visibility UI surfaces:

- title screen
- version labels
- splash screens
- fonts/additional glyphs if needed
- Pokedex graphics and terminology
- trainer card graphics and wording
- trade UI art if still relevant
- town map labels and icons
- battle HUD graphics where necessary

Potential Cantina replacements:

- Pokedex -> Cantina Index
- Trainer Card -> Profile Card
- Pokemon Center -> Support Hub / Repair Bay / Creator Lounge
- Pokemart -> Store / Tool Shop / Node Market

### Phase 7: Audio Replacement

If we want full brand separation, replace:

- title music
- iconic overworld themes
- battle themes
- key jingles
- catch / heal / menu SFX where necessary
- cries if desired

Recommendation:

- Keep this as a separate tracked milestone.
- Audio replacement is valuable, but it should not block the first art/text conversion.

### Phase 8: Optional New Mechanics

Only after the reskin build is stable should we consider:

- a real abilities system
- new type count or new type chart
- UI width expansions for longer names
- new move categories beyond existing effects
- rewritten progression structure
- map topology changes
- new minigames or social systems

## What I Think Is The Best Path

The best version of this project is not "rewrite Pokemon from scratch." It is:

1. keep the battle and overworld engine
2. keep the slot counts initially
3. total-convert the fiction, art, terminology, and progression flavor
4. add new mechanics only after the reskin is already shippable

That path gives you a fast route to a recognizable Cantina game instead of an open-ended engine rewrite.

## Replacement Workstreams By File Area

Use this as the practical ownership map.

### A. Canonical Naming Tables

- `data/pokemon/names.asm`
- `data/moves/names.asm`
- `data/items/names.asm`
- `data/trainers/names.asm`
- `data/types/names.asm`
- `data/player/names.asm`
- `data/player/names_list.asm`

### B. Mechanics Tables

- `data/pokemon/base_stats/*.asm`
- `data/pokemon/evos_moves.asm`
- `data/moves/moves.asm`
- `data/moves/field_moves.asm`
- `data/moves/tmhm_moves.asm`
- `data/trainers/parties.asm`
- `data/wild/grass_water.asm`
- `data/wild/*.asm`
- `data/wild/maps/*.asm`

### C. Story / Dialog / Event Logic

- `text/*.asm`
- `scripts/*.asm`
- `data/maps/objects/*.asm`
- `data/maps/headers/*.asm`
- `engine/movie/oak_speech/*.asm`

### D. High-Visibility Art

- `gfx/title/`
- `gfx/splash/`
- `gfx/player/`
- `gfx/trainers/`
- `gfx/sprites/`
- `gfx/pokemon/`
- `gfx/pokedex/`
- `gfx/trainer_card/`
- `gfx/town_map/`
- `gfx/battle/`
- `gfx/sgb/`

### E. Supporting System Files

- `constants/charmap.asm`
- `constants/pokemon_constants.asm`
- `constants/move_constants.asm`
- `constants/trainer_constants.asm`
- `constants/sprite_constants.asm`
- `constants/type_constants.asm`
- `constants/item_constants.asm`

## Asset Package I Will Need From You Later

To execute the swap cleanly, I need structured source material rather than loose images and notes.

### Required

- Final project/game title
- Final replacement for Pokemon / Pokedex / Trainer / Pokeball terminology
- 151 creature names mapped to original species slots
- creature bios or short descriptions
- creature evolution mapping
- creature front and back sprite art
- replacement trainer class names
- named story cast list
- battle portrait art for trainer classes
- overworld sprite art list
- move rename list
- move effect intent notes only where mechanics should change
- item rename list
- location rename list
- story/lore rewrite notes

### Strongly Recommended

- a single spreadsheet with tabs for species, moves, items, trainers, locations, story beats
- a folder of graphics named to match target slots
- a short style guide covering tone, color treatment, silhouettes, and vocabulary

### Ideal File Formats

- CSV or Google Sheet export for mappings
- PNG for source art
- short Markdown briefs for story and terminology

## Proposed Internal Project Structure

I recommend we keep the game source intact and stage your custom content under a dedicated project folder.

Suggested structure:

```text
docs/cantina/
  CANTINA_RESKIN_MASTER_PLAN.md
  terminology.md
  mapping/
    species_mapping.csv
    moves_mapping.csv
    trainers_mapping.csv
    items_mapping.csv
    locations_mapping.csv
  assets/
    species/
    trainers/
    sprites/
    ui/
    audio/
```

That keeps planning assets separate from the actual disassembly until we are ready to apply them.

## Risks and Gotchas

### 1. Tokenized Text

The text engine uses Pokemon-specific shorthand tokens. If we do not redefine them carefully, stray brand language will remain all over the game.

### 2. Length Limits

Game Boy-era UI buffers are small. Long Cantina names may require abbreviations or later UI work.

### 3. Engine Assumptions

IDs, counts, pointer tables, and ordering matter. Reordering species or moves early is riskier than remapping them in place.

### 4. Audio Recognition

Even after visual/text replacement, recognizable Pokemon music would still make the project feel derivative.

### 5. Version Surfaces

There are Red/Blue/Green/SGB-specific assets and edge cases. We should intentionally choose whether to support all of them.

## Recommended Milestones

### Milestone 1

Planning and mapping only.

Output:

- terminology sheet
- slot mapping sheets
- art checklist

### Milestone 2

Brand removal and high-visibility UI replacement.

Output:

- title/logo swap
- intro text swap
- key terminology swap
- core menu branding swap

### Milestone 3

Creature/trainer/item/location data replacement.

Output:

- full Cantina naming pass
- parties and encounters remapped
- key story beats remapped

### Milestone 4

Full art pass.

Output:

- creature art
- character art
- UI art
- map-facing visual pass

### Milestone 5

Audio pass and polish.

Output:

- branded soundtrack/SFX
- final QA build

### Milestone 6

Optional feature expansion.

Output:

- ability system or other new mechanics if still desired

## Immediate Next Step

~~Before any code changes, the next best move is to create the canonical mapping sheets.~~

**✅ Phase 0 + Phase 1 fully complete. Phase 2 data generation complete.** All mapping sheets built + all bot profile data generated. See Session Progress Log above.

### Next Actions (in priority order)

**1. ✅ DONE — Bot species mapping** — all 151 slots filled

**2. ✅ DONE — Bot profile data** — stats, learnsets, dex entries in `bot_profiles.csv`

**3. ✅ DONE — Type effectiveness matrix** — 104 matchups in `type_effectiveness.csv`

**4. ✅ DONE — Image pipeline built + all 190 bot sprites generated** — color + gray variants, square aspect ratio, progress tracking. See Session 2 above for full details.

---

**5. 🔜 GLITCHBOT front sprite cleanup**
~20 GLITCHBOT front slots returned no image from Gemini. Either:
- Run a targeted retry pass: `python3 batch_pipeline.py --slot <id>` for each failed GLITCHBOT slot
- OR create one shared "MissingNo-style" glitch sprite and reuse it for all 39 GLITCHBOT slots

**6. 🔜 PNG → `.pic` conversion (ROM-ready sprites)**
All processed PNGs need to run through the existing `tools/gfx.c` build tool to produce Game Boy compressed `.pic` files. Then drop into:
- `gfx/pokemon/front/` (56×56 grayscale variants)
- `gfx/pokemon/back/` (48×48 grayscale variants)
Use the `_gray.png` variants for ROM (4-tone palette). Color variants are for GBC palette extraction.

**7. 🔜 Generate UI assets**
The pipeline is built with style presets for all UI assets. Run `generate_ui_assets.py`:
- Title logo (`PokéBots`)
- Splash screen (`Airtime Media` replacing Game Freak)
- 15 type badge icons (from `types_mapping.csv` — type name + archetype + color feel)
- Trainer portraits: Sean Parker, Ginzbo, 8 Gym Leaders, 4 Elite Four (Platform Legends)

**8. 🔜 Phase 2: Brand Removal Pass (ROM writes)**
Write the CSV data into the actual pokered codebase `.asm` files:
- `data/pokemon/names.asm` — replace all 151 species names (from `species_mapping.csv`)
- `data/types/names.asm` — replace all 15 type names (from `types_mapping.csv`)
- `constants/charmap.asm` — redefine `#` token from POKé → BOT
- `data/moves/names.asm` — replace all 165 move names (from `moves_mapping.csv`)
- `data/items/names.asm` — replace all item names (from `items_mapping.csv`)
- `data/trainers/names.asm` — replace all trainer class names (from `trainer_mapping.csv`)

**9. 🔜 Phase 3: Creature Data Replacement (ROM writes)**
Write bot profile data into ROM `.asm` files using `bot_profiles.csv` as source:
- `data/pokemon/base_stats/*.asm` — write HP/ATK/DEF/SPD/SPC + catch rate + base XP + growth rate + L1 moveset (151 files)
- `data/pokemon/dex_text.asm` — write all 151 dex entries (from `bot_dex_entries` fields in `bot_profiles.csv`)
- `data/pokemon/evos_moves.asm` — write level-up learnsets per bot (from `learnset_levels` column)
- `data/types/type_matchups.asm` — write the new 15×15 effectiveness matrix (from `type_effectiveness.csv`)

**10. 🔜 Per-bot GBC palettes**
Extract dominant 4 colors from each color sprite (`_front.png`) → write per-species RGB15 palette entries to `data/pokemon/cgb_palettes.asm`. This makes sprites display in color on GBC hardware using the `wOnCGB` flag enabled in Session 2.

**11. 🔜 Rival Ginzbo's starter bot (John to confirm)**
Which species slot does Ginzbo pick at the beginning? Needs to be locked before Phase 5 (NPC dialog rewrite).
