# Glim-Default — Setting + Worked Example

This folder serves two purposes:

1. **The published default setting.** When a new player picks "the default Glim setting" during the campaign interview (`references/interview-guide.md`, Path D), the GM copies the `lore/` files from here into the new campaign and starts a fresh PC.
2. **A worked example of play.** The non-`lore/` files (`character-sheet.md`, `current.md`, `clocks.json`, `session-log.md`, etc.) show three sessions of an actual campaign in this setting, with the new oracle and clock mechanics annotated for reference.

---

## Setting Pitch

A low-fantasy world with flint-and-steel technology. Roughly 25 years ago, magic, monsters, and dungeons began appearing in the lands west of the homeland. The PC is part of a chartered expedition — Lantern Hold — into this new territory, which is held by sapient natives (**the Vahn**) whose magic is inherited shape-binding and whose relationship with the new monsters is fundamentally different from the settlers'. Tone: frontier survival, awe and dread at the magical, colonial moral weight.

---

## What's In Here

### World layer (the "default setting" — copy these into a new campaign)

| File | Purpose |
|------|---------|
| `lore/world/the-glim.md` | The phenomenon — what it is, how it manifests, who can use it |
| `lore/world/the-vahn.md` | The natives — bound-form magic, lines, monster cosmology, current stance |
| `lore/locations/lantern-hold.md` | The starting settlement — six-month-old palisade on bear-line gathering ground |
| `lore/characters/captain-rhel-daven.md` | The PC's commanding officer — full personality and history |

### Play layer (the "worked example" — do *not* copy into a new campaign)

| File | Purpose |
|------|---------|
| `character-sheet.md` | Toren Vesh — journeyman scout, Glim apprentice (one possible PC; new players make their own) |
| `current.md` | Mid-campaign state at end of Session 3 — active threads, NPCs, clocks render |
| `clocks.json` | Three active clocks + one archived clock with full step history and resolution narrative |
| `session-log.md` | Three session summaries with mechanics annotations (likelihood choices, boon/bane outcomes, clock fills) marked as teaching-only |
| `gm-notes.md` | Behind-the-screen — the actual answers (where Bren is, what the bear-stone is for, the captain's fallback plan) |
| `writing-guide.md` | Tone, prose rules, boundaries — copy and adapt for your own Glim-setting campaign |
| `advancement.md` | Campaign-tuned advancement triggers (Vahn contact, Glim breakthrough, dungeon survival) |

---

## Reading Order

If you're **learning the mechanics**, read in this order:

1. `lore/world/the-glim.md` and `lore/world/the-vahn.md` — get the world's shape
2. `session-log.md` — see three sessions of play with mechanics annotated
3. `clocks.json` — examine the audit trail (every tick logged with its trigger)
4. `current.md` — see how the play state is rendered for resumption
5. `gm-notes.md` — see the GM's hidden picture beneath the player-facing state

If you're **starting a new campaign in this setting**:

1. Read the four `lore/` files
2. Skim `writing-guide.md` to absorb the tone
3. Follow `references/interview-guide.md` Path D — the GM will walk you through character creation against this world

---

## How the Example Differs from a Fresh Campaign

The PC (Toren Vesh) is one possible scout-archetype character — when starting fresh, you build your own PC. Suggested starting roles are listed in the interview guide (scout, hedge mage, hired blade, settler with a craft, scholar/cartographer).

The mid-Session-3 state shows clocks at 4/6, 3/8, and 2/4 — a fresh campaign starts with whatever clocks the opening situation needs (typically zero or one).

The session log includes mechanics annotations (Die 1/2/3 values, likelihood settings, clock ticks). A real campaign log strips these — they're here purely as teaching annotations.

---

## Mechanics Demonstrated

The example was built specifically to exercise the polished system. Look for:

- **Three-die oracle** with weighted likelihoods (`unlikely`, `likely`, `fifty-fifty`)
- **Boon promoting plain → and** (Session 1 — captain disposition unexpectedly improved)
- **Bane promoting plain → and** on a No (Session 2 — eastern ridge "are we observed" rolled `No, and...`)
- **Cap-edge no-op** (boon on already-favorable elaboration does nothing — see oracle-guide.md for full rule)
- **Clock created and surfaced** ("Halric overdue", tactical, 2/4 by second watch)
- **Clock filling across sessions** ("Bear-line patience" — 0 → 4/6 over three sessions)
- **Clock completed and archived** ("Captain's assessment" — see `clocks.json` `completed` array)

Cross-reference `references/oracle-guide.md` and `references/clocks.md` to see the rule each annotation applies.

---

*This is a starter, not a sandbox. The setting deliberately leaves room for the player to fill in — the eastern woods, the deeper dungeons, the rest of the Vahn lines, the homeland's politics, the other charters. Run it, and the world will render as you go.*
