# Quick Reference

## Core Roll
`1d20 + Stat + Proficiency + Circumstance` vs DC

**Roll when:**
- Outcome uncertain AND failure interesting
- Calibrating character skill (practice, training, exploration)

**Don't roll:**
- Trivial or impossible actions
- Failure would stall the story

## DCs
| Difficulty | DC |
|------------|-----|
| Routine | 6 |
| Straightforward | 10 |
| Challenging | 14 |
| Difficult | 18 |
| Heroic | 22 |
| Legendary | 26+ |

## Stats & Proficiency
**Stats (0–6):** Physical, Technical, Social — chosen by *approach*, not task

**Same task, different stats:**

| Task | Physical | Technical | Social |
|------|----------|-----------|--------|
| Persuade a guard | Loom intimidatingly | Cite regulations | Charm them |
| Research a topic | All-night study session | Cross-reference sources | Ask the right people |
| Open a locked door | Kick it down | Pick the lock | Convince someone to open it |

**Proficiency:** Untrained +0 | Trained +2 | Expert +4 | Master +6 | Legendary +8

## NPC Rolls

When an NPC acts independently — pursuing their own goals, not reacting to the PC — roll for them using tiers. **Not for opposed rolls** — if the PC acts and an NPC resists, set a DC; don't roll for both sides.

| Tier | Modifier | Examples |
|------|----------|----------|
| Untrained | +1 | Civilian, out of their depth, frightened |
| Competent | +3 | Trained professional, doing their job |
| Expert | +5 | Veteran, specialist, this is what they're known for |
| Master | +7 | Best in the city, feared reputation |
| Legendary | +9 | Songs are sung, kingdom-wide renown |

Tier reflects skill at the *specific action*, not overall threat. A master duelist is Legendary at swordplay but might be Untrained at negotiation.

Apply circumstance modifiers (+2 to -4) for situational factors, just as with player rolls.

## Oracle (3 dice — always all three)

**Die 1 (d6) — yes/no, threshold by likelihood:**

| Likelihood | Yes on | % |
|------------|--------|---|
| Sure thing | auto-yes | 100 |
| Very likely | 2-6 | 83 |
| Likely | 3-6 | 67 |
| Fifty-fifty | 4-6 | 50 |
| Unlikely | 5-6 | 33 |
| Very unlikely | 6 | 17 |
| Impossible | auto-no | 0 |

**Die 2 (d6) — elaboration:** 1-2 `but` / 3-4 plain / 5-6 `and`. Independent of yes/no.

**Die 3 (d10) — boon/bane:** 1 bane / 2-9 neutral / 10 boon. Promotes Die 2 one step on PC favorability. Direction never flips.

Favorability ladder:
- On Yes: `but → plain → and` (and is best for PC)
- On No: `and → plain → but` (but is best — silver lining)

**Why Die 3?** Always-rolled boon/bane keeps the GM honest. 20% of the time fate forces a complication or windfall the GM didn't choose. See `oracle-guide.md` for full rationale.

**Oracle vs Roll:** Character *doing* something → roll. World *revealing* something → oracle. Set likelihood honestly first, then roll all three.

```bash
python scripts/dice.py oracle likely
python scripts/dice.py oracle-batch --likelihood likely "Thread 1" "Thread 2"
```

## NPC Priming

Prime *before* the player rolls — this shapes the DC and prevents yes-man GMing.

**When to prime:**
- First appearance in a session (what happened offscreen?)
- Player is about to attempt persuasion/deception/negotiation/intimidation
- Meaningful time has passed since last interaction

**Example prompts:**
- "Is [NPC] in a receptive mood?"
- "Has [NPC] learned something new?"
- "Is [NPC] predisposed toward suspicion/trust/urgency?"

Roll first, interpret second. The oracle reveals the NPC's state; the player roll determines if their approach works.

## Oracle for Internal States (Optional)
When character psychology is ambiguous, oracle can reveal it: "Does she enjoy this?" / "Is he aware of the change?"
Use when the player wants to *discover* their character, not dictate them. See `oracle-guide.md` for details.

## Pressure Clocks

| Scope | Default Size | Use For |
|-------|--------------|---------|
| Tactical | 4 | Scene pressure (guards arrive, fire spreads) |
| Encounter | 6 | A single arc (heist discovered, ally's patience) |
| Campaign | 8 | Long horizon (war approaches, secret revealed) |

**Surface protocol:** name the clock when you create it; show state at scene transitions and when an encounter starts; announce ticks. Hidden pressure goes in `gm-notes.md`, not on a clock.

**Tick triggers:** partial successes, bane elaborations on relevant oracles, time skips, scene transitions, narrative beats. Each tick needs a stated reason.

```bash
python scripts/clocks.py campaign/clocks.json create heist-discovered "The job is blown" 6 encounter
python scripts/clocks.py campaign/clocks.json tick heist-discovered --trigger "guard noticed the open door"
python scripts/clocks.py campaign/clocks.json complete heist-discovered --resolution "alarm tripped; they ran"
```

Full guide: `references/clocks.md`

## Stress Track
`0 Fresh → 1-2 Strained → 3-4 Desperate → 5 Broken`

**Stress is a GM tool** — apply when salvaging failures or softening consequences. Don't negotiate.

**Success at Cost:** Near-miss (1-2 under DC) can succeed + 1 stress. Never if it would hit 5.

## Story Points (3/session)
- **1pt:** Advantage on roll, creative invocation, reduce 1 stress
- **2pt:** Establish narrative fact

## Session Saves
**Offer at:** Scene conclusions, before time skips, new locations, significant character moments, when context is getting long.

**Before saving:** Discuss advancement if milestones were hit.

## Advancement Triggers
New proficiency, upgrade proficiency tier, or +1 stat (rare). Story Points reset to 3.

Discuss with player: *What did the character learn? What changed?*
