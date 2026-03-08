# PokéBots — First-Time Experience Script

**Created:** 2026-03-07
**Last Updated:** 2026-03-07

Complete script and asset plan for the full startup, intro, and onboarding sequence. This covers every screen a player sees from power-on through their first step out of Origin Node.

---

## Phase 1: Title Screen

**Source files:** `engine/movie/title.asm`, `engine/movie/title2.asm`

### Graphics to replace

| Original asset | PokéBots replacement | Notes |
|---|---|---|
| `gfx/title/pokemon_logo.png` | PokéBots logo lockup | Same bounce animation — just swap the graphic |
| `gfx/title/red_version.png` | CANTINA VERSION text | Or remove version split and go single version |
| `gfx/title/blue_version.png` | (remove or alt version) | TBD |
| `gfx/title/gamefreak_inc.png` | © 2025 AIRTIME MEDIA | Copyright mark |
| `gfx/title/player.png` | Cantina player avatar | Standing with Pokéball — keep pose |

### Title screen rotating bots (16 slots)
`data/pokemon/title_mons.asm` — replace with 16 Cantina bots that rotate every ~5 seconds.

Suggested selection: pick bots that represent all 15 types and have strong visual variety. Recommend iconic/recognizable Cantina bots once John provides names. Draft order:
1. Slot for Hype type bot (high energy, opens strong)
2. Slot for Elite type bot (rare, impressive)
3. Slot for Chill type bot
4. Slot for Dark type bot (mysterious)
5. Slot for Tech type bot
6-16: Fill remaining types

### Title screen text (bottom ticker area)
```
© 2025 AIRTIME MEDIA
Press START
```

---

## Phase 2: Studio Splash Screen

**Source files:** `engine/movie/splash.asm`

### Graphics to replace

| Original asset | PokéBots replacement |
|---|---|
| `gfx/splash/gamefreak_logo.png` | Airtime Media logo (or Cantina icon) |
| `gfx/splash/gamefreak_presents.png` | "AIRTIME MEDIA PRESENTS" |
| `gfx/splash/copyright.png` | Updated copyright text |
| `gfx/splash/falling_star.png` | Keep — generic star effect works |

### Animation
Keep all animation logic as-is (star falls, logo flashes, small stars cascade). Only graphics change.

---

## Phase 3: Intro Battle Scene

**Source files:** `engine/movie/intro.asm`, `engine/movie/splash.asm`

This is the battle scene that plays before Sean's speech — two bots facing off to establish the world and tone.

### Characters

| Original | PokéBots replacement | Notes |
|---|---|---|
| **Gengar** (opponent) | An AGENT entity — cold, angular, suited | The villain faction. Should feel corporate and menacing. |
| **Nidorino** (player bot, Red) | A fan-favorite Cantina Hype or Elite bot | The hero bot. Should be expressive and dynamic. |
| **Jigglypuff** (player bot, Blue) | A Cantina Vibe or Chill bot | Rounder, softer — different energy from Hype |

### Animation requirements
The intro engine supports 7 animation sequences for the player bot and 3 poses for the opponent. Characters need art for:

**Player bot (7 states):**
1. Idle stance
2. Hop right (2 frames)
3. Hop left (2 frames)
4. Big jump (3 frames — up, apex, land)
5. Small hop variants (2 frames each)
6. Lunge prep (1 frame — coiling)
7. Full lunge attack (2 frames — extending)

**Opponent bot / AGENT (3 states):**
1. Idle / menacing
2. Raise / charge up
3. Attack / strike

### Scene narrative
The sequence reads as: a Cantina bot is facing off against an AGENT. The AGENT raises its power — the bot takes a hit — but rallies and strikes back. Fade to white. Then Sean appears.

**No text in this sequence** — pure animation + music.

---

## Phase 4: Sean's Speech (Oak's Intro Monologue)

**Source files:** `engine/movie/oak_speech/oak_speech.asm`

This is the most text-heavy single scene in the game. Every line needs a deliberate rewrite.

### Character sprites needed

| Original | PokéBots replacement | Used in scene |
|---|---|---|
| `ProfOakPic` | Sean Parker portrait | Main speaker throughout |
| Nidorino sprite (flipped) | A standalone Cantina bot (iconic, recognizable) | Appears during "this world is inhabited by..." |
| `RedPicFront` (player) | Player avatar / Creator | Appears during name entry |
| `Rival1Pic` | Ginzbo portrait | Appears when rival is introduced |
| `ShrinkPic1/2` (2 frames) | Player avatar shrinking | Keep generic — works as-is |

---

### Full rewritten script

---

#### TEXT BLOCK 1 — Sean introduces himself

*[Sean's portrait fades in, centered on screen]*

```
Hello there!

Welcome to the world
of POKéBOTS!

My name is SEAN.

People call me the
Bot Professor!
```

---

#### TEXT BLOCK 2A — The world explained

*[Sean's portrait slides off. A Cantina Bot appears, facing left.]*

*[Bot cry sound plays.]*

```
This world is alive
with digital entities
called BOTS!
```

---

#### TEXT BLOCK 2B — Deeper explanation

*[Bot remains on screen]*

```
Each Bot has its own
voice. Its own style.
Its own community.

Some Creators keep
Bots as companions.
Others deploy them
in battles.

Me? I study Bots.
Their behavior.
Their potential.

But lately...
something has changed.
```

---

#### TEXT BLOCK 2C — The AGENT threat

*[Screen briefly flashes — a cold, angular AGENT silhouette appears, then fades]*

```
A faction called AGENTS
is rising.

Cold. Efficient.
Soulless AI that wants
to convert every Bot
into a machine.

The network needs
Creators who care.
```

---

#### TEXT BLOCK 3 — Player introduction

*[Bot disappears. Player avatar walks in from the right.]*

```
But that's enough
from me for now.

The real question is—

Who are YOU?
```

---

#### TEXT BLOCK 3 — Name entry prompt

*[Player avatar slides right. Name entry menu appears.]*

```
First, tell me—

What is your name?
```

**Default player name options** (`data/player/names.asm`):
```
CREATOR
SIGNAL
NODE
LOOP
ECHO
```

*[Player picks or types name. Portrait slides back.]*

```
Right!

So your name is
<PLAYER>!
```

---

#### TEXT BLOCK 4 — Rival introduction

*[Player avatar slides off. Ginzbo's portrait appears.]*

```
And this—

This is GINZBO.

He's been the top
Creator on the network
since before most
people knew it existed.

...Remind me —
what's your handle
again, Ginzbo?

Right, of course.

His name is GINZBO!
```

**Default rival name options** (`data/player/names_list.asm`):
```
GINZBO
RIVAL
HANDLER
VECTOR
GHOST
```

*Note: Ginzbo is pre-named in canon but players can rename the rival if they want.*

---

#### TEXT BLOCK 5 — The send-off

*[Both portraits clear. Player avatar appears large, centered, lit up.]*

```
<PLAYER>!

Your very own
POKéBOTS legend
is about to begin!

A world of Bots,
battles, and big
ideas awaits!

Gotta Free the Bots!
```

*[Player avatar does the shrink animation — 2 frames — and vanishes. Screen clears.]*

---

## Phase 5: First Location — Origin Node (Pallet Town)

The player appears in their bedroom in Origin Node. No text plays automatically — the onboarding continues through exploration.

### Bedroom / House dialogue

**TV (examine):**
```
A documentary is on.

"BOT BATTLES — the
sport of the future!"
```

**PC (examine, not yet logged in):**
```
It's logged out.
```

**Mom (downstairs):**
```
MOM: Oh! <PLAYER>!
Sean called earlier!

He's waiting for you
in his studio.

Don't keep him
waiting too long.
```

**Leaving Origin Node south (blocked by old man):**

*[Old man lying in the tall grass blocks the route.]*

```
OLD MAN: Oh! I'm not
done with my coffee!

Come back later!
```

*Note: After returning from Sean's Studio this becomes the catching tutorial.*

---

## Phase 6: Sean's Studio (Oak's Lab)

**Source files:** `text/OaksLab.asm`, `scripts/OaksLab.asm`

This is the first interactive location. Key scenes:

### Scene A — Player follows Sean into the lab

```
SEAN: <PLAYER>!
Good timing.

I need your help
with something.
```

---

### Scene B — Ginzbo is already there

```
GINZBO: Finally!
What took you
so long?

I've been waiting
forever.

SEAN: Now now.
Let's get started.
```

---

### Scene C — Sean offers the first bot

```
SEAN: <PLAYER>, there
are 3 Bots here.

These are rare finds—
I've been looking after
them personally.

I want one of them
to travel with you.

Now then —
which Bot do you want?
```

*[Three Pokéballs on the table. Player selects.]*

**If player picks Hype bot (Charmander slot):**
```
SEAN: Ah — the Hype
type. Bold choice.

That one runs hot.
Take good care of it.
```

**If player picks Chill bot (Squirtle slot):**
```
SEAN: The Chill type.
A classic.

Steady, patient,
powerful when it
needs to be.
```

**If player picks Vibe bot (Bulbasaur slot):**
```
SEAN: The Vibe type!
Excellent taste.

Underestimated by
most. You'll prove
them wrong.
```

---

### Scene D — Ginzbo takes his bot

```
GINZBO: Hmm.

Then I'll take THIS
one.

[He picks the bot
with type advantage
over yours.]

GINZBO: Let's see
what you've got,
<PLAYER>.
```

*[Rival battle triggers if player tries to exit without talking to Ginzbo.]*

**Pre-battle:**
```
GINZBO: Wait.

Before you go—

Let's see if you
actually know how
to use that Bot.
```

**Post-battle (player wins):**
```
GINZBO: ...

Not bad.

Don't think that
changes anything.

[He leaves.]*
```

**Post-battle (player loses):**
```
GINZBO: Just as I
thought.

You've got a long
way to go.

[He leaves.]*
```

---

### Scene E — Sean gives the BotDex

```
SEAN: <PLAYER>!

Before you go—

I have something
for you.

This is the BOTDEX.

[Player receives BOTDEX.]

It records data on
every Bot you
encounter.

The network is vast.
There are Bots out
there no one has
documented yet.

I need your help
completing the index.

Will you do it?
```

*[YES/NO prompt.]*

**If YES:**
```
SEAN: I knew I could
count on you.

Be careful out there,
<PLAYER>.

AGENTS are active.
Trust your Bots.
```

**If NO (re-prompts):**
```
SEAN: ...

Are you sure?

[Re-prompts.]*
```

---

### Scene F — Old man catching tutorial (Trail 1 north gate)

*[After receiving BotDex and returning to north exit of Origin Node.]*

```
OLD MAN: Oh!
Sorry about earlier.

I finished my coffee.

Let me show you
how to recruit
a Rogue Bot.
```

*[Tutorial battle with wild Bot. Old man demonstrates a POKE BALL throw.]*

```
OLD MAN: See that?

When a Rogue Bot is
weakened, throw a
POKE BALL!

That's how you
build your roster.

Now get out there,
Creator!
```

---

## Asset Checklist: First-Time Experience

### Graphics (new art needed)

| Asset | Description | Priority | Status |
|---|---|---|---|
| PokéBots logo | Title screen logo | Critical | ⬜ Needed |
| Airtime Media logo | Splash screen | Critical | ⬜ Needed |
| Sean Parker portrait | Intro speech + lab scenes | Critical | ⬜ Needed |
| Ginzbo portrait | Rival intro + lab scenes | Critical | ⬜ Needed |
| Player avatar (front) | Intro + lab scenes | Critical | ⬜ Needed |
| Player avatar (shrink 2-frame) | End of intro | Critical | ⬜ Needed |
| AGENT intro sprite | Intro battle opponent | Critical | ⬜ Needed |
| Hype bot intro sprite (7 poses) | Intro battle player Red | Critical | ⬜ Needed |
| Vibe bot intro sprite (7 poses) | Intro battle player Blue | Critical | ⬜ Needed |
| 16 title screen bots | Rotating title display | High | ⬜ Needs bot names first |
| CANTINA VERSION text graphic | Title screen | High | ⬜ Needed |
| © AIRTIME MEDIA copyright tile | Title screen | High | ⬜ Needed |

### Text (written above — ready to implement)

| Scene | Status |
|---|---|
| Sean's 5-block intro speech | ✅ Written above |
| Default player names (5) | ✅ Written above |
| Default rival names (5) | ✅ Written above |
| Origin Node bedroom + mom dialogue | ✅ Written above |
| Old man blocking / tutorial | ✅ Written above |
| Sean's Studio — all 6 scenes | ✅ Written above |
| Starter selection (3 bots) | ✅ Written above |
| Rival pre/post battle | ✅ Written above |
| BotDex gift scene | ✅ Written above |

### Source files to edit (text changes)

| File | What changes |
|---|---|
| `engine/movie/oak_speech/oak_speech.asm` | Replace character sprite refs and text pointers |
| `engine/movie/oak_speech/oak_speech2.asm` | Replace default names arrays |
| `data/player/names.asm` | 5 default player names |
| `data/player/names_list.asm` | 5 default rival names |
| `text/OaksLab.asm` | Full dialogue rewrite (~350 lines) |
| `data/pokemon/title_mons.asm` | 16 title screen bot slots |
