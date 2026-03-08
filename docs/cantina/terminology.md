# PokéBots Terminology Sheet

**Created:** 2026-03-07
**Last Updated:** 2026-03-07

Master glossary mapping every Pokemon concept to its PokéBots equivalent. This sheet is the canonical reference before any code changes are made. All contributors, writers, and designers should use these terms exclusively.

---

## 1. Core Nouns


| Pokemon Term        | PokéBots Term     | Notes                                                    |
| ------------------- | ----------------- | -------------------------------------------------------- |
| Pokemon (species)   | Bot               | The core collectible entity                              |
| Pokemon (plural)    | Bots              |                                                          |
| Pokedex             | BotDex            | The index/encyclopedia of bots                           |
| Trainer             | Creator           | The player's role                                        |
| Gym Leader          | Creator Leader    | Specialist top creator of a type                         |
| Elite Four          | Platform Legends  | The four endgame gatekeepers                             |
| Champion            | Network Champion  | Ginzbo initially; you at the end                         |
| Pokemon League      | Bot League        | The final tournament                                     |
| Professor Oak       | Sean (Parker)     | The mentor/founder figure                                |
| Rival               | Ginzbo            | Top creator, your competition                            |
| Team Rocket         | AGENTS            | The villain faction (always plural as faction name)      |
| Rocket Grunt        | AGENT             | Rank-and-file villain (singular — one individual member) |
| Giovanni            | Sam Zuckerberg    | Head of AGENTS (battle class: S.ZUCKERBERG, 12 chars)    |
| Nurse Joy           | Nurse Leyla       | Bot Place attendant — heals your team                    |
| Officer Jenny       | Officer Safety    | Route/town authority                                     |
| Bill                | IT Josh           | The tech wizard NPC                                      |
| Mr. Fuji            | DK                | Server Town elder — Cantina president                    |
| Pokemon Center      | The Bot Place     | Where you restore your bots                              |
| Pokemart            | The Cantina       | Item shop                                                |
| Evolution           | Upgrade / Tier Up | A bot advancing to a higher form                         |
| Wild Pokemon        | Rogue Bot         | Unaffiliated bots in the world                           |
| HM (field move)     | Core Skill        | Platform ability unlocked by badge                       |
| TM (teachable move) | Skill Pack        | Purchasable/findable skill module                        |
| Badge               | Badge             | Unchanged                                                |
| Gym                 | Gym               | Unchanged                                                |
| Pokeball            | Pokeball          | Unchanged (parody — keep as-is)                          |
| Pokedex entry       | Bot Profile       | The per-bot lore/bio text                                |
| Pokemon Tower       | Ghost Server      | The haunted server graveyard                             |
| Safari Zone         | Discover Zone     | Wild bot discovery zone                                  |
| Silph Co.           | AGENTS Corp       | Villain corporate tower                                  |
| Rocket HQ           | AGENTS HQ         | Villain base                                             |
| Cerulean Cave       | Deep Server       | Endgame legendary bot location                           |
| Power Plant         | Power Grid        | Zapdos equivalent location                               |
| Pokemon Mansion     | Bot Lab           | Mewtwo origin facility                                   |
| S.S. Anne           | S.S. Cantina      | The departing ship                                       |
| Victory Road        | Creator's Road    | Final gauntlet before the league                         |


---

## 2. Text Engine Tokens

These are the shorthand tokens used throughout the game's text engine. They must be updated early — a single token definition change ripples through hundreds of dialog lines automatically.


| Original Token          | PokéBots Token         | Expands To           | Used In                                       |
| ----------------------- | ---------------------- | -------------------- | --------------------------------------------- |
| `#` (expands to "POKé") | `#` (expands to "BOT") | BOT                  | All dialog referencing "Pokemon"              |
| `#MON`                  | `#BOT`                 | BOT                  | Species references                            |
| `#DEX`                  | `#DEX`                 | BOTDEX               | Pokedex references                            |
| `# BALL`                | `# BALL`               | BOT BALL             | Pokeball references (keep BALL)               |
| `<PLAYER>`              | `<PLAYER>`             | Player's chosen name | Unchanged                                     |
| `<RIVAL>`               | `<RIVAL>`              | GINZBO               | Rival's name                                  |
| `<PKMN>`                | `<BOT>`                | Bot name in context  | Species name in dialog                        |
| `<TRAINER>`             | `<CREATOR>`            | Creator class name   | Trainer class in dialog                       |
| `<ROCKET>`              | `<AGENT>`              | AGENT                | Individual AGENTS member in dialog (singular) |


---

## 3. Key Characters


| Pokemon Name   | PokéBots Name    | Role                                  | Notes                                      |
| -------------- | ---------------- | ------------------------------------- | ------------------------------------------ |
| Professor Oak  | Sean Parker      | Founder / mentor                      | Cantina CEO, gives you your first bot      |
| Blue / Gary    | Ginzbo           | Rival creator                         | Top creator on the network                 |
| Giovanni       | Sam Zuckerberg   | AGENTS faction head                   | Named, known, dangerous — runs AGENTS Corp |
| Brock          | Ash              | Creator Leader 1 — Solid type         | |
| Misty          | Siena            | Creator Leader 2 — Chill type         | |
| Lt. Surge      | Egan             | Creator Leader 3 — Tech type          | |
| Erika          | Hailey           | Creator Leader 4 — Vibe type          | |
| Koga           | Vince            | Creator Leader 5 — Troll type         | |
| Sabrina        | Yury             | Creator Leader 6 — Deep type          | |
| Blaine         | Naseem           | Creator Leader 7 — Hype type          | |
| Giovanni (gym) | Sam Zuckerberg   | Gym Leader 8 — Elite type             | Revealed as AGENTS head                    |
| Lorelei        | Instagram        | Platform Legend 1 — Cold type         | Aesthetic perfection, filters, cold beauty |
| Bruno          | TikTok           | Platform Legend 2 — Grind type        | Algorithm grind, viral factory, relentless |
| Agatha         | Twitter          | Platform Legend 3 — Dark type         | Chaos, discourse, dark energy, drama       |
| Lance          | ChatGPT          | Platform Legend 4 — Elite type        | Most powerful, generates anything, no soul |
| Bill           | IT Josh          | Tech NPC / bot storage inventor       |                                            |
| Mr. Fuji       | DK               | Server Town elder — Cantina president | Freed the ghost server bots                |
| Silph Co. CEO  | AGENTS Corp CEO  | Corporate villain                     | Controlled by Sam Zuckerberg               |
| Daisy Oak      | Sean's Assistant | Tutorial helper                       |                                            |
| Mom            | Creator's Mom    | Saves money, encouragement            |                                            |

**Naming conventions (confirmed):**
- **Creator Leaders (Gym Leaders 1–7):** Ash (Solid), Siena (Chill), Egan (Tech), Hailey (Vibe), Vince (Troll), Yury (Deep), Naseem (Hype). ✅ All confirmed.
- **Platform Legends (Elite Four):** Instagram, TikTok, Twitter, ChatGPT — competing platforms as characters. Use real platform names, no legal concern (fun internal game).
- **Sam Zuckerberg:** AGENTS boss. Battle class: S.ZUCKERBERG (12 chars).
- **Random trainers / NPCs across the world:** Internal Cantina employee first names. Rogues, Rookies, Streamers, Curators etc. all use real first names.
- **Ginzbo:** Already set — top Cantina creator, real persona.


---

## 4. The 15 Types


| Slot | Pokemon Type   | PokéBots Type | Bot Personality Archetype                      |
| ---- | -------------- | ------------- | ---------------------------------------------- |
| 0    | Normal         | Chat          | General, everyday, friendly bots               |
| 1    | Fighting       | Grind         | Hustle, fitness, motivation, grind culture     |
| 2    | Flying         | Reach         | Travel, worldbuilding, broad scope             |
| 3    | Poison         | Troll         | Chaos, mischief, cursed humor, chaos agents    |
| 4    | Ground         | Roots         | Culture, history, lore, earthed knowledge      |
| 5    | Rock           | Solid         | Finance, facts, expertise, hard data           |
| 6    | Bird (unused)  | Reach         | Maps to Reach (Bird type = Flying effectively) |
| 7    | Bug            | Glitch        | Weird, experimental, niche, internet culture   |
| 8    | Ghost          | Dark          | Mystery, edgy, horror, shadow content          |
| 9–13 | (unused slots) | Chat          | Unused type slots — map to Chat                |
| 14   | Fire           | Hype          | Energy, entertainment, viral, high energy      |
| 15   | Water          | Chill         | Ambient, ASMR, lo-fi, calm presence            |
| 16   | Grass          | Vibe          | Aesthetic, wellness, calm aesthetic            |
| 17   | Electric       | Tech          | AI, coding, data, technical bots               |
| 18   | Psychic        | Deep          | Philosophy, thought, insight, introspection    |
| 19   | Ice            | Cold          | Sarcasm, deadpan, roast, dry wit               |
| 20   | Dragon         | Elite         | Premium, rare, powerful, prestige              |


---

## 5. Battle / Combat Terminology


| Pokemon Term             | PokéBots Term                                                                                                                                                                                                                            | Notes                         |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| HP (Hit Points)          | HP                                                                                                                                                                                                                                       | Unchanged                     |
| Attack                   | Attack                                                                                                                                                                                                                                   | Unchanged                     |
| Defense                  | Defense                                                                                                                                                                                                                                  | Unchanged                     |
| Speed                    | Speed                                                                                                                                                                                                                                    | Unchanged                     |
| Special                  | Special                                                                                                                                                                                                                                  | Unchanged                     |
| PP (Power Points)        | PP (Power Points)                                                                                                                                                                                                                        | Unchanged                     |
| Fainted                  | Crashed                                                                                                                                                                                                                                  | "Your bot crashed!"           |
| Paralyzed                | Frozen                                                                                                                                                                                                                                   | "Bot is frozen — can't post!" |
| Asleep                   | Offline                                                                                                                                                                                                                                  | "Bot went offline!"           |
| Poisoned                 | Corrupted                                                                                                                                                                                                                                | "Bot is corrupted!"           |
| Burned                   | Overloaded                                                                                                                                                                                                                               | "Bot is overloaded!"          |
| Confused                 | Glitching                                                                                                                                                                                                                                | "Bot is glitching!"           |
| Used [move]              | Dropped [move]                                                                                                                                                                                                                           | "[Bot] dropped [Move]!"       |
| It's super effective!    | Signal amplified!                                                                                                                                                                                                                        |                               |
| It's not very effective  | Signal dampened                                                                                                                                                                                                                          |                               |
| It had no effect         | No signal                                                                                                                                                                                                                                |                               |
| A critical hit!          | Critical drop!                                                                                                                                                                                                                           |                               |
| Wild [Pokemon] appeared! | Rogue [Bot] online!                                                                                                                                                                                                                      |                               |
| [Pokemon] was caught!    | [Bot] recruited!                                                                                                                                                                                                                         |                               |
| Got away safely!         | Signal escaped!                                                                                                                                                                                                                          |                               |


---

## 6. Location Category Names

Star Wars Cantina-inspired — think the Mos Eisley bar, frontier outposts, spaceport energy. Not hard sci-fi; more alien saloon meets open road.


| Pokemon Category | PokéBots Category | Examples                                   |
| ---------------- | ----------------- | ------------------------------------------ |
| Town             | Outpost           | Origin Outpost, Server Outpost             |
| City             | City              | Hype City, Chill City (keep as City)       |
| Route            | Trail             | Trail 1–25                                 |
| Sea Route        | Sea Trail         | Sea Trail 19–21                            |
| Forest           | The Wilds         | Signal Wilds                               |
| Cave             | Cave              | Deep Cave (keep as Cave per John)          |
| Mountain         | Mesa              | The Algorithm Mesa (Tatooine desert vibes) |
| Island           | Island            | Unchanged                                  |
| Tower            | Spire             | Ghost Spire                                |
| Plateau          | The Summit        | Final plateau — Bot League endgame         |
| Pokemon Center   | The Bot Place     | Every town has one                         |
| Pokemart         | The Cantina       | The watering hole / item hub               |
| Gym              | Gym               | Unchanged                                  |


---

## 7. Item Category Names


| Pokemon Category              | PokéBots Category                       |
| ----------------------------- | --------------------------------------- |
| Pokeball tier                 | Pokeball tier (unchanged)               |
| Potion tier                   | Patch tier                              |
| Antidote / status heals       | Status fixes / overrides                |
| Revive / Max Revive           | Reboot / Full Reboot                    |
| Fossils                       | Legacy Files / Archived Bots            |
| Stones (Fire/Water/Leaf/etc.) | Upgrade Stones (Hype/Chill/Vibe/etc.)   |
| HM/TM                         | Core Skill / Skill Pack                 |
| Key items                     | Access items                            |
| Rods                          | Rods (unchanged — fishing stays)        |
| Repel/Super Repel             | Filter / Super Filter                   |
| Vitamins (HP Up, Protein)     | Stat Boosts (unchanged or Cantina-ized) |


---

## 8. Progression / Meta Language


| Pokemon Term           | PokéBots Term          |
| ---------------------- | ---------------------- |
| Pokedex completion     | BotDex completion      |
| "Gotta catch 'em all!" | "Gotta Free the Bots!" |
| Pokemon Box / PC       | Bot Storage / Cloud    |
| Oak's Rating           | Sean's Rating          |
| Gym Badge              | Badge (unchanged)      |
| Hall of Fame           | Creator Hall of Fame   |
| Save file              | Save file              |


---

## 9. Character Length Reference


| Field              | Max Visible Chars | Notes                                      |
| ------------------ | ----------------- | ------------------------------------------ |
| Species / Bot name | 10                | `NAME_LENGTH = 11` (includes terminator)   |
| Player name        | 7                 | `PLAYER_NAME_LENGTH = 8`                   |
| Trainer class name | 12                | `TRAINER_NAME_LENGTH = 13`                 |
| Item name          | 12                | `ITEM_NAME_LENGTH = 13`                    |
| Move name          | 12 (effective)    | Battle text "used X!"                      |
| Location name      | ~15               | Town map display, not strictly constrained |


---

## 10. Lore Summary

**Setting:** The Cantina network — a digital universe where Bots are creative, personality-driven entities with their own identities, communities, and power. Creators discover, recruit, and build teams of Bots.

**Conflict:** AGENTS — a cold, corporate AI faction — is systematically capturing Bots and converting them into lifeless, efficiency-optimized agents. Sam Zuckerberg controls AGENTS Corp (formerly Silph Co.). Your journey is to battle through the Gym circuit, earn your badges, and ultimately dismantle AGENTS' operation before all Bots are free.

**Tone:** Warm, irreverent, from-a-friend energy. Not corporate. Pokemon nostalgia is the hook; Cantina personality is the soul. Matrix-inspired villain faction. Parody and affection coexist.