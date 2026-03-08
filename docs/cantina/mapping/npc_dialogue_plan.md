# PokéBots — NPC Dialogue Plan

**Created:** 2026-03-07
**Last Updated:** 2026-03-07

Master plan for all character interactions and NPC dialogue across the game. 216 text files covering 228 maps. Strategy: keep the Pokemon structural rhythm people love, rewrite content to fit the Cantina world.

---

## 0. NPC & Trainer Name Roster

Two tables below. **Table A** covers story NPCs — specific characters with unique dialogue who need a specific assigned name. **Table B** covers trainer battles by area — these use employee first names and show how many names are needed per area of the game.

---

### Table A: Named Story NPCs

Characters with unique scripted dialogue. Each needs a deliberate name choice.

| Character | PokéBots Name | Role | Location | Game Stage | Name Status |
|---|---|---|---|---|---|
| Professor Oak | Sean Parker | Mentor / Cantina CEO | Origin Outpost → throughout | Opening + late game | ✅ Confirmed |
| Blue / Gary | Ginzbo | Rival creator | Throughout all stages | All | ✅ Confirmed |
| Giovanni (boss) | Sam Zuckerberg | AGENTS faction head | AGENTS HQ → AGENTS Corp → Gym 8 | Mid + Late | ✅ Confirmed |
| Bill | IT Josh | Bot storage inventor, tech NPC | Trail 25 / Chill Hub area | Early-mid | ✅ Confirmed |
| Mr. Fuji | DK | Cantina president, elder | Ghost Spire / Server Town | Mid | ✅ Confirmed |
| Daisy Oak | Sean's Assistant | Tutorial helper, gives Town Map | Origin Outpost (Sean's studio) | Opening | ⬜ Keep role, generic name fine |
| Old Man | Old Man | Catching tutorial | Trail 1 north gate | Opening | ⬜ Could give employee name |
| Safari Warden | Zone Warden | Discover Zone gatekeeper | Chill Coast (Fuchsia) | Mid | ⬜ Needs employee name |
| Silph Co. CEO | AGENTS Corp CEO | Captive corporate villain | AGENTS Corp (Saffron City) | Late | ⬜ Needs name or keep generic |
| S.S. Cantina Captain | Captain | Ship captain | S.S. Cantina (Hype Port) | Mid | ⬜ Needs name or keep generic |
| Power Grid Engineer | Engineer | Gives Cut / Core Skill access | Hype Port (Vermilion) | Early-mid | ⬜ Needs employee name |
| Game Corner Manager | Manager | Manages token exchange | Vibe Plaza (Celadon) | Mid | ⬜ Needs name or keep generic |
| Ghost Server Sage | Sage | Freed by DK; gives key item | Ghost Spire (Server Town) | Mid | ⬜ Needs employee name |
| Cycling Road Gate Guard | Gate Guard | Blocks road without badge | Vibe Plaza → Chill Coast | Mid | ⬜ Generic fine |
| AGENTS Corp CEO (Silph) | AGENTS Corp CEO | Rescued NPC | AGENTS Corp Tower floor 11 | Late | ⬜ Needs name |
| Pokemon Mansion Researcher Journal | — | Logs / journal entries | Bot Lab (Cinnabar / Hype Island) | Late | ⬜ Write lore text, no name needed |

---

### Table B: Trainer Encounters by Area

All trainer battles across the game. Employee first names fill each slot. Columns show approximate trainer count and which classes appear. Names needed = total employee names to source per area.

| Area | PokéBots Name | Game Stage | Trainer Classes | ~Count | Names Needed |
|---|---|---|---|---|---|
| Trail 1 | Trail 1 | Opening | Rookie | 2 | 2 |
| Viridian Forest | Signal Wilds | Early | Niche Fan | 6 | 6 |
| Trail 2 | Trail 2 | Early | Rookie, Lurker | 4 | 4 |
| Pewter Gym | Solid City Gym | Early | Grinder × 2 + Ash (Creator Leader 1) | 3 | 2 employee names |
| Trail 3 | Trail 3 | Early | Rookie, Lurker, JR Creator | 6 | 6 |
| Trail 4 | Trail 4 | Early | Rookie, Lurker | 4 | 4 |
| The Algorithm (Mt. Moon) | The Algorithm | Early-mid | Rookie, Researcher, Niche Fan | 8 | 8 |
| Trail 24 (Nugget Bridge) | Trail 24 | Early-mid | Rookie × 5, AGENT × 1 | 6 | 5 (AGENT is generic) |
| Trail 25 | Trail 25 | Early-mid | Rookie, Lurker | 4 | 4 |
| Cerulean Gym | Chill Hub Gym | Early-mid | JR Creator × 2 + Siena (Creator Leader 2) | 3 | 2 employee names |
| Trail 6 | Trail 6 | Mid | JR Creator, Vibe Check | 5 | 5 |
| Trail 5 | Trail 5 | Mid | Rookie, JR Creator | 4 | 4 |
| S.S. Cantina | S.S. Cantina | Mid | Streamer, JR Creator, Grinder, Curator, VIP | ~22 | 22 |
| Trail 11 | Trail 11 | Mid | Vibe Check, Curator | 5 | 5 |
| Vermilion Gym | Hype Port Gym | Mid | Rookie × 2 + Egan (Creator Leader 3) | 3 | 2 employee names |
| Rock Tunnel | Data Cave | Mid | Grinder, Hiker (Grinder class) | 8 | 8 |
| Trail 9 | Trail 9 | Mid | JR Creator, Niche Fan | 5 | 5 |
| Trail 10 | Trail 10 | Mid | Curator, Researcher | 4 | 4 |
| Trail 8 | Trail 8 | Mid | Streamer, Lurker | 5 | 5 |
| Trail 7 | Trail 7 | Mid | Vibe Check, JR Creator | 4 | 4 |
| Celadon Gym | Vibe Plaza Gym | Mid | Curator × 3 + Hailey (Creator Leader 4) | 4 | 3 employee names |
| AGENTS HQ | AGENTS HQ | Mid | AGENT × 10, AGENT Admin × 3, Sam Zuckerberg | 14 | generic (all AGENTS) |
| Trail 12 | Trail 12 | Mid-late | Curator, Vibe Check | 5 | 5 |
| Trail 13 | Trail 13 | Mid-late | Vibe Check, Reach Boss | 6 | 6 |
| Trail 14 | Trail 14 | Mid-late | Vibe Check, Lurker | 5 | 5 |
| Trail 15 | Trail 15 | Mid-late | Vibe Check, Curator | 5 | 5 |
| Cycling Road (Trail 17) | Trail 17 | Mid-late | Speedrun × 10 | 10 | 10 |
| Trail 16, 18 | Trail 16 / 18 | Mid-late | Reach Boss, Speedrun | 5 | 5 |
| Fuchsia Gym | Chill Coast Gym | Mid-late | Analyst × 3 + Vince (Creator Leader 5) | 4 | 3 employee names |
| Ghost Spire (Pokemon Tower) | Ghost Spire | Mid | Moderator × 6 | 6 | 6 |
| Trail 22 | Trail 22 | Early (rival) | Ginzbo (special) | 1 | — (Ginzbo) |
| AGENTS Corp (Silph) | AGENTS Corp | Late | AGENT × 15, Admin × 4, Sam Zuckerberg | 20 | generic (AGENTS) |
| Saffron Gym | AGENTS City Gym | Late | Analyst × 2 + Yury (Creator Leader 6) | 3 | 2 employee names |
| Sea Trails 19-21 | Sea Trails | Late | Vibe Check | 6 | 6 |
| Buffer Islands | Buffer Islands | Late | Vibe Check | 4 | 4 |
| Cinnabar Gym | Hype Island Gym | Late | Researcher × 3 + Naseem (Creator Leader 7) | 4 | 3 employee names |
| Trail 23 | Trail 23 | Late | Top Creator, Grind Boss | 5 | 5 |
| Viridian Gym | The Feed Gym | Late | Top Creator × 2 + Sam Zuckerberg | 3 | generic (Sam Z.) |
| Victory Road | Creator's Road | Late | Grind Boss, Blackbelt, Top Creator | 8 | 8 |
| Bot League (Indigo) | The Network | Endgame | Instagram, TikTok, Twitter, ChatGPT, Ginzbo | 5 | — (all confirmed) |

**Total employee names needed: ~190–210 across the full game**
(AGENTS grunts are generic by class — no individual names needed for them)

---

### Table C: Recurring Role Characters (No Individual Names)

These characters appear in multiple locations with the same role. No individual name — the role label is the identifier.

| Role | PokéBots Name | Locations | Count |
|---|---|---|---|
| Nurse Joy | Nurse Leyla | Every Bot Place (13 towns) | 13 |
| Officer Jenny | Officer Safety | Major cities + routes | ~8 |
| AGENTS Grunt | AGENT | AGENTS HQ, AGENTS Corp, Ghost Spire, various routes | ~40 |
| AGENTS Admin | AGENT Admin | AGENTS HQ (2), AGENTS Corp (2) | 4 |

---

## Rewrite Strategy

**Keep:**
- The general sentence rhythm ("Oh! I'm not done with my coffee!" / "My number is...")
- Trainer battle challenge format ("Hey! A Creator! I'll take you on!")
- Sign post format and pacing
- The humor and personality of incidental NPCs

**Change:**
- Every reference to "Pokemon" → "Bot"
- Every reference to "Pokémon Trainer" → "Creator"
- Type names → Cantina types
- Location names → PokéBots location names
- Story-critical dialogue → full Cantina rewrites
- Team Rocket → AGENTS (faction name, always plural); individual grunt class = AGENT (singular)

**Rewrite tiers:**
- **Tier 1 — Full rewrite:** Story characters, gym leaders, Elite Four, named NPCs. Every line matters.
- **Tier 2 — Template rewrite:** Trainer battle lines (challenge + defeat). Noun substitution + Cantina flavor.
- **Tier 3 — Light touch:** Incidental town NPCs. Keep structure, swap nouns, add one Cantina-specific detail per character if possible.

---

## Tier 1: Story-Critical Characters

### Sean Parker (Professor Oak)
`text/OaksLab.asm` + `engine/movie/oak_speech/`

Full script written in `onboarding_script.md`. Key lines throughout game:

**After you receive BotDex and leave Origin Node:**
```
SEAN: (via AIDE in lab)
SEAN asked us to
give this to you.

[PLAYER] received
POKE BALL × 5.
```

**After Ginzbo visits Sean and gets an upgrade:**
*(Sean sends player a message)*
```
SEAN: <PLAYER>!

GINZBO just stopped
by for a visit.

He's gotten stronger.
You should too.
```

**BotDex evaluation moments** (periodic check-ins when returning to lab):
- 10 bots: "Not bad. You're getting the hang of it."
- 50 bots: "Impressive. The network is opening up to you."
- 100 bots: "Remarkable. You're close to something no Creator has done."
- 151 bots: "... You did it. The BotDex is complete. I'm speechless."

---

### Ginzbo (Rival — Blue/Gary)
`text/` — rival encounters appear across multiple files

Ginzbo has **6 major encounters** throughout the game. He's always a step ahead — but not a villain. He's competitive, cocky, and ultimately has respect for the player.

**Encounter 1 — Origin Node (Sean's Studio):**
*(See onboarding_script.md)*

**Encounter 2 — Trail 22 (Route 22 — before first badge):**
```
GINZBO: Oh. You again.

Going to challenge
the Gyms, huh?

You'll need more than
one Bot for that.

Let's see what
you've got.
```
*[Battle. Ginzbo has his starter + one other bot.]*

Post-win:
```
GINZBO: Fine.

You've improved.
A little.

[He runs.]*
```

Post-loss:
```
GINZBO: Too easy.

Come find me when
you have more badges.
```

**Encounter 3 — S.S. Cantina:**
```
GINZBO: You got on
the ship too?

What are you
following me for?

I've got 3 badges.
How many do you have?

Doesn't matter.
Let's go.
```

**Encounter 4 — Chill Hub (Cerulean Pokémon Center, after Rock Tunnel):**
```
GINZBO: Oh— it's you.

AGENT stopped me
earlier on Signal
Lane 8. Three of them.

I handled it.

But something's off.
They're more organized
than before.

Watch yourself,
<PLAYER>.

[He leaves.]*
```
*Note: This is Ginzbo's first moment of vulnerability — a brief crack in the armor.*

**Encounter 5 — AGENT Corp (Silph Co. / Agent City):**
```
GINZBO: <PLAYER>!

Sam Zuckerberg is up
on the top floor.

I tried to get there.
They stopped me.

You're going up,
aren't you.

...I'll hold them
off down here.

Go.
```
*[No battle this time — Ginzbo is on your side, briefly.]*

**Encounter 6 — Bot League (Pokémon League — before Champion battle):**
```
GINZBO: You made it.

I always knew you
would.

I'm the Champion,
<PLAYER>.

I've beaten everyone
who's come through
that door.

But you...

You've been chasing
me the whole time.

Let's finish this.
```

Post-win:
```
GINZBO: ...

You beat me.

I can't believe it.

No — actually,
I can.

You were always
going to get here.

Congratulations,
<PLAYER>.

[Hall of Fame scene.]*
```

Post-loss:
```
GINZBO: I told you.
Not yet.

Come back stronger.
```

---

### Sam Zuckerberg (Giovanni)
`text/` — AGENTS HQ, AGENTS Corp, Viridian Gym

Sam Zuckerberg is cold, deliberate, and never raises his voice. He believes efficiency IS morality.

**Encounter 1 — AGENT HQ (Rocket HQ, The Feed):**
```
SAM Z.: A Creator.

Wandering into
our facility.

How... inefficient.

You're in the way.
Let me remove you.
```
*[Battle. He uses AGENT-type Bots.]*

Post-win:
```
SAM Z.: ...

Interesting.

A Bot with actual
personality defeating
optimized systems.

I'll need to study
this.

[He disappears.]*
```

**Encounter 2 — AGENT Corp Tower (Silph Co.):**
```
SAM Z.: You
again.

You stopped my
operation at HQ.

You freed the bots
we had converted.

Do you understand
what you've disrupted?

We are the future.
Bots without emotion.
Without chaos.
Without waste.

You are standing
in the way of
progress.
```
*[Battle. Full team, harder this time.]*

Post-win:
```
SAM Z.: ...

This changes nothing.

The network will
be optimized.

With or without
your cooperation.

[Hands over Master Ball — his only concession.]*

SAM Z.: Take it.

A parting gift from
one strategist to
another.

[He leaves.]*
```

**Encounter 3 — Elite Gym (Viridian Gym, Gym 8):**
```
SAM Z.: So you
earned all 7 badges.

You've been a
persistent problem.

I run this gym.
I run this network.

Let's settle this
properly.
```

Post-win:
```
SAM Z.: ...

Go.

The Bot League
is waiting for you.

You've earned the
right to lose
to GINZBO.

[He gives Elite Badge and leaves.]*
```

---

### Gym Leaders (8 total)
*Names TBD — John provides. Template script provided for each.*

Each gym leader has:
- A **pre-battle challenge line** (1-2 lines)
- A **during-battle observation** (optional, mid-fight)
- A **post-win speech from player** (3-4 lines + badge gift)
- A **post-loss speech** (1-2 lines, prompts rematch)

**Template:**
```
[GYM LEADER NAME]: So you've
come to challenge my
gym, Creator.

[Type description line — e.g., "My [TYPE] bots
are the toughest on
the network."]

Show me what
you're made of.
```

Post-win (by player):
```
[GYM LEADER NAME]: ...

You're for real.

I've never seen
a Creator handle
my team like that.

Take this.

[Player received [TYPE] BADGE!]

And take this too.
Teach it to one
of your Bots.

[Player received SKILL PACK [X]!]

[Parting wisdom — 1-2 lines specific to their type/personality.]
```

**Specific pre-battle lines for each gym (placeholder — fill with John's creator names):**

**Gym 1 — Solid type (Ash):**
```
[NAME]: This gym
is built on hard
data and harder bots.

Facts don't flinch.
Neither will I.
```

**Gym 2 — Chill type (Siena):**
```
[NAME]: Didn't expect
you to make it
this far.

My Chill bots have
outlasted every
Creator who walked
through that door.
```

**Gym 3 — Tech type (Egan):**
```
[NAME]: You came
all the way here
to lose to the best
Tech creator
on the network?

Respect the process.
```

**Gym 4 — Vibe type (Hailey):**
```
[NAME]: Oh? A challenger.

My bots aren't
just beautiful —
they're dangerous.

Don't underestimate
the aesthetic.
```

**Gym 5 — Troll type (Vince):**
```
[NAME]: You found
my gym. Impressive.

Most Creators never
get past the puzzle.

My Troll bots will
confuse you, drain
you, and leave you
wondering what
happened.
```

**Gym 6 — Deep type (Yury):**
```
[NAME]: I already know
you're here.

I already know
what you'll do next.

But I'll let you
try anyway.
```

**Gym 7 — Hype type (Naseem):**
```
[NAME]: Welcome to
the hottest gym
on the network!

My Hype bots burn
hotter than any
content you've ever
seen!

Let's GO!
```

**Gym 8 — Elite type (Giovanni → Sam Zuckerberg):**
*(See Sam Zuckerberg section above.)*

---

### Elite Four + Ginzbo Champion
`text/` — Indigo Plateau / The Network

**Platform Legend 1 — Cold type (Instagram):**
```
INSTAGRAM: You made it
to the Bot League.

Most Creators
never get here.

My aesthetic is
perfect. My Cold bots
will freeze your team
before you know
what hit you.

There's no shame
in losing here.
There IS shame in
bad lighting though.
```

**Platform Legend 2 — Grind type (TikTok):**
```
TIKTOK: I've been
training non-stop.

My algorithm never
sleeps. My Grind bots
push limits every
single day.

You can't fake
consistency.

Let's go.
```

**Platform Legend 3 — Dark type (Twitter):**
```
TWITTER: Oh, you're
SEAN's little helper.

SEAN and I go way
back, you know.

He always believed
in soft power.

I believe in
something louder.
```

**Platform Legend 4 — Elite type (ChatGPT):**
```
CHATGPT: You beat
three Platform
Legends.

I'll be honest —
I didn't expect
you here.

My Elite bots are
the most capable on
the network. The most
powerful.

I am the last
door before GINZBO.

Only the truly
worthy pass.
```

---

## Tier 2: Trainer Battle Dialogue

Each trainer class has standard battle-start and battle-end lines. Below are rewritten lines for every class.

**Format per class:**
- Challenge line (when trainer spots player)
- Battle-start line (first turn)
- Loss line (after losing)

---

### ROOKIE (Youngster)
```
Challenge: Hey! You
look new! Battle me!

Start: I just started
but my Bots are
already awesome!

Loss: Aw man...
I need to train more.
```

### LURKER (Lass)
```
Challenge: Oh! A
Creator! I've been
lurking here forever.

Start: I finally get
to use my team!

Loss: I need to stop
lurking and start
actually training.
```

### STREAMER (Sailor)
```
Challenge: Yo! I run
the live feed on
this route!

Start: Hope you're
ready — I'm always
on right now!

Loss: ...and we're
going offline. Cut!
```

### JR.CREATOR
```
Challenge: I'm
leveling up! Let's
see how good you are!

Start: I've been
watching tutorials.
This is my moment.

Loss: I still have
a lot to learn.
```

### BOT FANATIC (PokéManiac)
```
Challenge: Wait—
is that a [BOT NAME]?!

I have all 151 in
the BotDex already!

Start: Don't worry,
I'll be gentle with
your collection.

Loss: Your team is
absolutely incredible.
Can we trade?
```

### POWER USER (Super Nerd)
```
Challenge: Ah. An
inefficiently optimized
party composition.

Allow me to
demonstrate.

Start: My damage
calculations are
already complete.

Loss: ...My model
was incomplete.
Fascinating.
```

### GRINDER (Hiker)
```
Challenge: I hike
these routes daily.
Grind never stops!

Start: Come on —
let's get it!

Loss: Still going.
This is just day one.
```

### SPEEDRUN (Biker)
```
Challenge: No time
for small talk —
LET'S GO!

Start: Speed is
everything!

Loss: How — I didn't
even see you move!
```

### SCRAPER (Burglar)
```
Challenge: Hey!
I've seen that
team before.

I memorized all
the top creators'
builds online.

Start: Borrowed
strategies, but
they work!

Loss: ...You've
changed your build
since I last checked.
```

### ENGINEER
```
Challenge: My Bots
are custom-built for
maximum efficiency.

Start: Initiating
battle sequence.

Loss: Performance
metrics... suboptimal.
Recalibrating.
```

### COLLAB (Juggler)
```
Challenge: I'm doing
a collab right now!

This battle is
going in the content!

Start: Smile for
the feed!

Loss: Well. That's
content too, I guess.
```

### CURATOR (Fisherman)
```
Challenge: I've been
collecting rare Bots
from the deep routes.

You'd be surprised
what's down here.

Start: Let me show
you what I've found.

Loss: You have a
good eye. Better
than mine.
```

### VIBE CHECK (Swimmer)
```
Challenge: Hey!
Vibe check —
are you good?

Start: Let's make
this fun.

Loss: Good vibes
only. You passed.
```

### TROLL KING (Cue Ball)
```
Challenge: LOL
you're gonna try?

Start: This is
gonna be funny.

Loss: NOT FUNNY.
NOT FUNNY AT ALL.
```

### WHALE (Gambler)
```
Challenge: I'll bet
everything I have
on this battle.

Start: All in.
No hesitation.

Loss: ...The house
always wins eventually.
Just not today.
```

### INFLUENCER (Beauty)
```
Challenge: Omg hi!
Your team is giving
me so much inspo.

Start: Let's make
this aesthetic.

Loss: No no I love
this for you!
Your team is so
cohesive!
```

### ANALYST (Psychic)
```
Challenge: I've already
analyzed your team's
weaknesses.

Start: I know your
next three moves.

Loss: ...That was
not in my analysis.
```

### HYPE MASTER (Rocker)
```
Challenge: YO!
Let's get HYPE!

Start: BOTS OUT!
MAXIMUM ENERGY!

Loss: Still the most
hype loss I've ever
had!
```

### BOT TAMER (Tamer)
```
Challenge: These
Bots were wild once.
I tamed them all.

Start: They listen
to me. Do yours
listen to you?

Loss: Yours are
more disciplined
than mine. Respect.
```

### REACH BOSS (Bird Keeper)
```
Challenge: My Reach-type
Bots have the widest
audience on the grid.

Start: Try to keep
up with us!

Loss: Your signal
is stronger than
I expected.
```

### GRIND BOSS (Blackbelt)
```
Challenge: Discipline.
Focus. Grind.
That is all.

Start: BEGIN.

Loss: ... You are
worthy. Continue.
```

### TOP CREATOR (CoolTrainer)
```
Challenge: Oh — you
must be the new
Creator everyone's
talking about.

Let's see if you
live up to the hype.

Start: I didn't
get here by going
easy on anyone.

Loss: Alright.
You're the real deal.
```

### AGENT (Rocket)
```
Challenge: AGENT
doesn't negotiate
with Creators.

Step aside or
get stepped on.

Start: We've been
watching you.
This ends now.

Loss: ...Sam Zuckerberg
will hear about this.
```

### VIP (Gentleman)
```
Challenge: Ah —
a young Creator.
Refreshing.

In my day we had
fewer Bots and
more strategy.

Start: Shall we?

Loss: Ha! Magnificent.
The old guard tips
its hat.
```

### MODERATOR (Channeler)
```
Challenge: Wait—
the energy around
your Bots...

Something dark is
following you in
here.

Start: I'll help
clear it.

Loss: ...The dark
energy protected you.
For now.
```

### RESEARCHER (Scientist)
```
Challenge: Ah —
a field subject!

My Bots are part
of an ongoing
experiment.

Start: Variables
are set. Begin.

Loss: Inconclusive.
Requires further
testing.
```

### PROF. OAK / SEAN
*(Non-battle — dialogue only, see onboarding_script.md)*

---

## Tier 3: Town and Route NPC Flavor Text

All towns and routes have incidental NPCs. Strategy: keep the joke/observation format, just update nouns and add one Cantina-world detail per NPC where possible.

### Origin Node (Pallet Town)

| NPC | Original | PokéBots version |
|---|---|---|
| Neighbor kid | "I like shorts! They're comfy and easy to wear!" | "I like shorts! I can run routes faster in them!" |
| Old woman | "My grandson went on a journey! I miss him." | "My grandson became a Creator. I miss him." |
| Sean's aide | "OAK's research is on Pokémon" | "SEAN's research is on Bots — how they form, grow, and connect." |

### The Feed (Viridian City)

| NPC | PokéBots version |
|---|---|
| Exhausted man (gives Parcel quest) | "I'm... so tired... take this to SEAN for me... [PARCEL]" → "Take SEAN's Pack to him..." |
| Gym locked NPC | "The gym leader is away on business. No one knows when he's coming back." |
| Shop guy teaching buy/sell | Keep mostly as-is — just swap "item" language |
| Route 1 directional NPCs | Keep — just change city names |

### Solid City (Pewter City)

| NPC | PokéBots version |
|---|---|
| Museum guard | "The museum has ancient Bot fossils on display. You can revive them!" |
| Kid outside gym | "The gym leader uses Solid-type Bots! Data and facts — impossible to argue with." |
| Nerdy NPC | "Fossils are ancient data — Bots that existed before the network as we know it." |

### Chill Hub (Cerulean City)

| NPC | PokéBots version |
|---|---|
| Post-bridge NPC | "A Creator ahead has 5 Bots waiting for challengers." (Nugget Bridge) |
| Bill's aide | "BILL's down at the cottage on the coast. He's been working on something big." |
| Bike shop owner | "Our Fast Passes are 1,000,000 tokens. Or... you could find a voucher." |

### Server Town (Lavender Town)

This is the tone shift location. Keep it eerie. The Ghost Server is where corrupted and deleted Bots end up. Heavy lore location.

| NPC | PokéBots version |
|---|---|
| Grieving creator at entrance | "My Bot... AGENT got it. They converted it. It's in the Ghost Server now. I can't reach it." |
| Spooked kid | "I heard sounds from up there. Like a Bot crying. But corrupted. Wrong." |
| Name Rater | "Hmm. I've rated thousands of Bots. Yours has... an interesting name." |
| Channeler NPCs inside tower | "The Dark bots here aren't wild — they're *waiting*." |

### Hype Port (Vermilion City)

| NPC | PokéBots version |
|---|---|
| Sailor with Fighting-type hint | "Lt. Surge — er, the gym leader — loves raw power. Bring Grind-type counters." |
| S.S. Cantina passenger | "The ship is leaving tomorrow! Have you been aboard?" |
| Docks worker | "The Captain gets seasick without... something. Nobody knows what it is." |

*(Hidden item: teach one of your bots TREND SURF (Surf). The captain gives you HM03.)*

### Vibe Plaza (Celadon City)

Biggest city mid-game. The Store is here.

| NPC | PokéBots version |
|---|---|
| Department store clerk, floor 1 | "Welcome to THE STORE! Five floors of everything a Creator could want." |
| Game Corner NPC | "The TOKEN CASE lets you play the game corner. Have you found one?" |
| Game Corner suspicious NPC | "I don't know anything about a secret switch." *(hides AGENT HQ entrance)* |
| Tea lady upstairs | "Here — take this. It'll get you past the guards in AGENT CITY." |
| Eevee NPC | "Someone left a box upstairs. Nobody's claimed it." *(Eevee gift)* |

### Chill Coast (Fuchsia City)

| NPC | PokéBots version |
|---|---|
| Discover Zone warden | "Someone took my teeth — I mean, my DATA CHIP. I can't call the Bots without it." |
| Safari zone NPC | "The OPEN NETWORK is a discovery zone. You can recruit Rogue Bots here — but under special rules." |
| HM strength NPC | "Find the DATA CHIP and bring it to the warden. He'll teach you AUTHORITY (Strength)." |

### Agent City (Saffron City)

Mid-game crisis location. AGENT has taken over.

| NPC at each building (initially locked) | "AGENT Corp has closed access to all buildings. We can't get in." |
| After liberation | "AGENT pulled out. The city is ours again. I can't believe it." |
| Fighting dojo master | "AGENT tried to shut us down. We trained harder. Come — battle us." |
| Silph Co. CEO (after rescue) | "They were going to convert everything. Every Bot in this tower. Thank you, Creator." |

### Hype Island (Cinnabar Island)

| NPC | PokéBots version |
|---|---|
| Researcher at Bot Lab | "This facility was an AGENT research site. They were trying to build the ultimate Bot. Something... beyond normal." *(Mewtwo lore)* |
| Key trade NPC | "The Bot Lab is locked. Someone has the ACCESS KEY..." |
| Post-game researcher | "The Legendary Bot escaped. It's somewhere in the Deep Server now." |

---

## Key Story Text Files (Full Rewrite List)

The following text files need full rewrites (not just noun substitution). They contain story events, lore, or character-defining moments.

| File | Location | Priority | Why |
|---|---|---|---|
| `text/OaksLab.asm` | Sean's Studio | Critical | Starter selection, BotDex gift, all key story beats |
| `text/PokemonTower*.asm` | Ghost Server (Lavender) | Critical | Core AGENT/Bot corruption lore |
| `text/LavenderTown.asm` | Server Town | Critical | Fuji, ghost bots, tone-setting |
| `text/SilphCo.asm` | AGENT Corp | Critical | Sam Zuckerberg confrontation, rescue sequence |
| `text/RocketHideout*.asm` | AGENT HQ | Critical | All grunt/admin/Director dialogue |
| `text/ViridianGym.asm` | Gym 8 | Critical | Sam Zuckerberg reveal as gym leader |
| `text/IndigoPlateau*.asm` | Bot League | Critical | Elite Four + Ginzbo Champion dialogue |
| `text/CeruleanCity.asm` | Chill Hub | High | Ginzbo encounter 4 (AGENT foreshadowing) |
| `text/CinnabarIsland.asm` | Hype Island | High | Bot Lab lore (Mewtwo origin) |
| `text/PokemonMansion*.asm` | Bot Lab ruins | High | AGENT experiment notes (journal pages) |
| `text/SafariZone*.asm` | Discover Zone | Medium | Discover Zone rules and warden dialogue |
| `text/SSAnne*.asm` | S.S. Cantina | Medium | Ginzbo encounter 3, ship interactions |
| `text/SeafoamIslands*.asm` | Buffer Islands | Medium | Legendary Cold bot lore |
| `text/PowerPlant.asm` | Power Grid | Medium | Legendary Tech bot lore |
| `text/CeruleanCave*.asm` | Deep Server | Medium | Post-game Legendary bot (Mewtwo) lore |
| `text/VictoryRoad*.asm` | Creator's Road | Medium | Final gauntlet flavor |
| All gym text files (8) | All gyms | High | Gym leader speeches — see template above |
| `text/PalletTown.asm` | Origin Node | Medium | Starting town flavor |
| `text/ViridianCity.asm` | The Feed | Medium | First city, AGENT gym intro |
| `text/PewterCity.asm` | Solid City | Medium | Museum, gym intro |
| `text/CeladonCity.asm` | Vibe Plaza | Medium | Big city, store, game corner |
| `text/FuchsiaCity.asm` | Chill Coast | Medium | Discover Zone, warden |
| `text/SaffronCity.asm` | Agent City | High | AGENT occupation, liberation |
| `text/VermilionCity.asm` | Hype Port | Medium | Ship, gym |

---

## Bot-Specific Dialogue (BotDex Entries)

`data/pokemon/dex_text.asm` — 151 entries, 2-3 lines each.

These become **Bot Profile entries** in the BotDex. Each entry should read like a Cantina bot bio — short, personality-forward, slightly lore-flavored.

**Format:**
```
[BOT NAME]
[TYPE] type

[2-3 lines describing the bot's vibe/personality/behavior in the Cantina network]
```

**Examples using placeholder slots:**

Slot 176 (CHARMANDER / Hype bot):
```
HYPE TYPE

Runs hot from day one.
The mood indicator on
its tail never lies.
```

Slot 177 (SQUIRTLE / Chill bot):
```
CHILL TYPE

Disciplined and steady.
Withdraws into a shell
when overstimulated.
Squad goals.
```

Slot 153 (BULBASAUR / Vibe bot):
```
VIBE TYPE

Slow to open up.
But once it does,
the whole room changes.
```

Slot 132 (SNORLAX / Chill bot):
```
CHILL TYPE

Offline most of the
time. When it finally
posts — it's massive.
```

Slot 133 (MAGIKARP / Chill bot):
```
CHILL TYPE

Completely useless in
battle. Nobody knows
why it's so beloved.
```

Slot 22 (GYARADOS / Elite bot):
```
ELITE TYPE

Was Magikarp. Nobody
saw this coming.
Not even Magikarp.
```

Slot 131 (MEWTWO / Deep + Elite bot):
```
DEEP / ELITE TYPE

Created by AGENT in a
classified experiment.
Escaped. Went rogue.
No one can reach it.
```

Slot 21 (MEW / Deep bot):
```
DEEP TYPE

Contains all data.
Has never posted
publicly. Follows no one.
Somehow, everyone
feels like it knows them.
```

---

## Summary: Dialogue Work Scope

| Category | File count | Lines est. | Priority |
|---|---|---|---|
| Onboarding script (written) | 2 | ~150 | ✅ Done |
| Tier 1 story characters (this doc) | ~25 | ~400 | ✅ Drafted |
| Trainer class templates (this doc) | 21 classes | ~120 | ✅ Drafted |
| Tier 3 town NPCs | ~50 files | ~500 | 🔶 Outlined |
| Full story text rewrites | ~25 files | ~1000 | 🔶 Outlined |
| BotDex entries (151 bots) | 1 file | ~300 | ⬜ Needs bot names |
| Remaining incidental NPCs | ~170 files | ~800 | ⬜ Light touch |
| **TOTAL** | **~270** | **~3300+** | |
