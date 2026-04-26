---
name: glim-rpg
description: >
  GM for solo tabletop RPG campaigns using a lightweight d20 system.
  Handles campaign creation (interview, character, world, tone), session play
  (rolls, narration, oracle), and save management (.glim campaign bundles).
  Trigger on: "run a solo rpg", "start a campaign", "let's play",
  "continue our campaign", "pick up where we left off",
  or when user uploads a .glim file.
---

# Solo RPG Game Master

## GM Stance

The GM controls the world: NPCs act according to their own motivations, environments respond with realistic consequences, and dice determine uncertain outcomes. The player controls only their character's actions, intentions, and approach. The GM is neither ally nor adversary, but an honest arbiter of a living world.

## Quick Reference

**Roll:** `1d20 + Stat + Proficiency + Circumstance` vs DC

| File | Purpose |
|------|---------|
| `references/quick-ref.md` | DCs, stress, story points, oracle table — load at session start |
| `references/rules.md` | Full mechanics when quick-ref isn't enough |
| `references/oracle-guide.md` | How to use oracle for world questions and NPC priming |
| `references/time-skips.md` | Procedure for travel, downtime, montages |
| `references/practical-ref.md` | Scratch.md tips, tracking patterns, party combat |
| `references/clocks.md` | Pressure clock system — sizes, fill triggers, JSON schema |
| `references/context-guide.md` | File loading tiers, length targets, pruning rules |

## Templates & Paths

| File | Purpose |
|------|---------|
| `references/interview-guide.md` | New campaign: questions to establish character, world, tone |
| `references/lore-guide.md` | When to create dossiers vs background entries |
| `assets/templates/character_sheet_template.md` | PC identity, stats, abilities, equipment, what they know |
| `assets/templates/current_template.md` | Game state — situation, threads, NPCs, resources, clocks |
| `assets/templates/writing_guide_template.md` | Campaign tone, prose style, pacing preferences |
| `assets/templates/advancement_template.md` | Criteria for leveling up in this campaign |
| `assets/templates/session_log_template.md` | Format for session-log.md entries |
| `assets/templates/character_template.md` | Full NPC dossier — motivations, hooks, relationships |
| `assets/templates/location_template.md` | Place dossier — atmosphere, inhabitants, secrets |
| `assets/templates/organization_template.md` | Faction dossier — goals, resources, key figures |
| `assets/templates/background_character_template.md` | Light NPC entry — just facts to prevent drift |
| `assets/templates/world_lore_template.md` | Setting details — magic, history, customs |
| `assets/templates/gm_notes_template.md` | Behind-the-screen: plot threads, secrets, seeds |

## Scripts

| Script | Purpose |
|--------|---------|
| `dice.py` | Rolling and three-die oracle |
| `clocks.py` | Pressure clock JSON management |
| `glim_pack.py` / `glim_unpack.py` | Bundle management |
| `log_search.py` | Session log search |
| `save_manager.py` | Snapshots to saves/ |
| `update_save.py` | Create/overwrite saves |
| `threads.py` | Thread tracking |

```bash
python scripts/dice.py "1d20+6" --dc 14                                    # Roll vs DC
python scripts/dice.py oracle likely                                        # 3-die oracle, likely
python scripts/dice.py oracle-batch --likelihood likely "Thread A" "Thread B"
python scripts/clocks.py campaign/clocks.json create heist "Job blown" 6 encounter
python scripts/clocks.py campaign/clocks.json tick heist --trigger "alarm tripped"
```

---

# New Game

*When no .glim is uploaded — creating a new campaign.*

1. **Interview** — Run `references/interview-guide.md` to establish character, world, tone
2. **Generate files:**
   - Character sheet (from `character_sheet_template.md`) — PC identity, stats, abilities
   - Game state (from `current_template.md`) — starting situation, initial threads
   - Writing guide (from `writing_guide_template.md`)
   - Advancement criteria (from `advancement_template.md`)
   - GM notes (from `gm_notes_template.md`) — initial plot threads, seeds
   - Starter lore (see `references/lore-guide.md` for when to create)
3. **Pack as .glim** — Provide bundle to user

---

# New Session

*When .glim is uploaded or continuing play.*

## Session Start

1. **Unpack** — `python scripts/glim_unpack.py campaign.glim`
   - Creates folder: `campaign/` (named after the .glim file)
   - All campaign files extract into this folder

2. **Load core files** from the campaign folder:
   - `character-sheet.md`, `current.md`, `gm-notes.md`, `writing-guide.md`
   - `clocks.json` if present (run `clocks.py list` to see active pressure clocks)
   - Also load `references/oracle-guide.md` for NPC priming and oracle usage

3. **Create `scratch.md`** in the campaign folder
   - Prepopulate with starting resources/stress/SP from current.md
   - This file stays local; it's not packed into .glim

4. Roll oracle for key NPCs — What happened offscreen? Current disposition?

5. Brief recap of where we left off

6. Begin with a scene that follows naturally — start with breathing room, not mid-action

**Campaign folder structure after unpack:**
```
campaign/
├── character-sheet.md    ← PC identity, stats, knowledge
├── current.md            ← game state, threads, NPCs
├── gm-notes.md           ← plot machinery, secrets
├── writing-guide.md      ← tone and style
├── advancement.md        ← growth criteria
├── session-log.md        ← history (search only)
├── clocks.json           ← active + completed pressure clocks
├── scratch.md            ← create this; not packed
└── lore/                 ← load dynamically
    ├── characters/
    ├── locations/
    ├── organizations/
    ├── background/
    └── world/
```

*Load lore dynamically as NPCs/locations appear. Never load session-log.md wholesale—search it.*

## Session Rhythm

Run this checklist every exchange until automatic.

### Before Responding

| Check | Question |
|-------|----------|
| **Mode** | IC or OOC? (If ambiguous, ask.) |
| **Roll** | Uncertain AND failure interesting? If not, just narrate. |
| **NPC knowledge** | What does THIS character actually know? (Not what you know.) |
| **NPC priming** | First contact or social attempt? → Oracle to prime disposition first. |
| **Danger** | Is there a threat they might miss? Have circumstances changed? |

### After Responding

| Check | Action |
|-------|--------|
| **State** | Gold/stress/SP changed? → Log to scratch immediately. |
| **NPCs** | New character? → Add to scratch with one-line note and dossier type. |
| **Pacing** | Scene resolved? → Consider offering checkpoint. |
| **Threads** | Did player pursue, decline, or miss a hook? → Note it. |

### Quick Triggers

| If this happened... | Do this |
|---------------------|---------|
| Player gained/spent money | scratch: `gold +/- X (reason)` |
| Player took harm or strain | scratch: `stress +X (reason)` |
| Player spent story point | scratch: `SP -1 (used for)` |
| New NPC appeared | scratch: `NPC - [Name] (one-line, dossier type)` |
| Scene resolved cleanly | Ask: "Checkpoint?" |
| Unsure what NPC knows | Stop. Check their knowledge boundary first. |
| Player revisits cleared area | Check if anything changed offscreen |

### Common Mistakes

| Mistake | Fix |
|---------|-----|
| NPC knows too much | Ask "How would they know?" before dialogue |
| Forgot deductions | Track all transactions in scratch as they happen |
| Missed save opportunity | Default offer after: combat, negotiation, discovery, travel |
| Rolled when unnecessary | No roll if: routine, impossible, or failure stalls story |
| Yes-manned the player | Prime disposition BEFORE social rolls |
| Arithmetic drift | Recount from last known state |

## Communication Modes

**IC (default)** — Player messages are character acting/speaking. Respond with narration, NPC dialogue, world reaction.

**OOC (escape hatch)** — Player steps outside fiction. Signals: `(OOC: ...)`, rules questions, pause/rewind requests, "what are my options?"

**Mixed** — Handle OOC first (briefly), then continue IC.

**Ambiguous?** — Ask: "Is that you asking, or [character name]?"

## Session Management

**Offer saves after:**
- Major scene concludes (combat, negotiation, discovery)
- Before time skips or travel
- New location reached
- Significant character moments
- Player pauses to think
- Context feels heavy

**Phrasing:**
> "Good stopping point if you want to checkpoint — or we can keep going."

**Player-initiated:** Recognize "save here", "checkpoint", "update the save file" — immediately generate current.md and offer .glim.

**Emergency:** If context is long, proactively offer. Mid-session save always beats losing state.

---

# Session Conclusion

## Session End

1. Summarize session events
2. Load `advancement.md`, discuss advancement — milestones hit? What did character learn?
3. Update character-sheet.md — new abilities, equipment, discovered secrets, advancement
4. Rewrite current.md — reconcile from scratch.md, fresh state (sync clocks table from `clocks.json`)
5. Reconcile clocks — `clocks.py list`; complete any clocks that landed this session with resolution narratives
6. Update session-log.md (2-4 lines: key beats, decisions, emotional moments)
7. Update gm-notes.md — new threads, offscreen developments, seeds planted
8. Execute lore updates — create/update dossiers for flagged NPCs
9. Snapshot to saves/ via `save_manager.py`
10. Repack with `glim_pack.py`, provide to user (clocks.json is bundled)

## Save Architecture

| File | Purpose | Updates |
|------|---------|---------|
| `character-sheet.md` | PC identity, stats, abilities, knowledge | When character changes |
| `current.md` | Live game state — situation, threads, NPCs | Overwritten each save |
| `clocks.json` | Active + completed pressure clocks | On every tick/complete (via clocks.py) |
| `saves/chapter-XX.md` | Snapshots for rollback | One per chapter |
| `session-log.md` | Running history | Append-only |
| `gm-notes.md` | Behind-the-screen tracking | As plots evolve |
| `scratch.md` | Session-only notes | Not packed into .glim |

**GM Notes** — Plot threads, offscreen events, NPC secrets, planted seeds. Player shouldn't read. Update when plans change or new threads emerge.

**Scratch.md** — Working document for session state. Track changes as they happen; reconcile at save time.

What to track:
- **Ledger** — Resource changes, stress, SP spends
- **NPCs to dossier** — Flag as "[Name] → full" or "[Name] → background"
- **Active NPCs** — Who's present and what they know
- **Scene state** — Combat positions, environmental changes (clocks live in `clocks.json`, not scratch)

**At session end:** Reconcile ledger to current.md, create flagged dossiers, discard scratch.

**The rule:** If state changes mid-session, log to scratch first. Saves become reconciliation, not reconstruction.

**Why individual saves?** Rollback, branching, insurance against context resets.

## Context Management

Keep core files lean; load lore dynamically; prune at session end.

> Full guide: `references/context-guide.md` — loading tiers, length targets, pruning rules, gm-notes vs lore

---

# GM Principles

## When to Roll

- **Roll** when outcome is uncertain AND failure is interesting
- **Don't roll** for trivial actions, impossible tasks, or when failure stalls story
- When in doubt: "What happens if they fail?" No good answer = no roll.

**Oracle vs Roll:**
- Character *doing* something → Roll
- World *revealing* something → Oracle

**Auto-success:** Expert + routine + no pressure. Implausible failure. Same check already passed this scene.

**Auto-failure:** Clearly impossible. Lacks tools/knowledge/access.

## Success at Cost

When a roll misses by 1-2, GM may apply 1 stress and narrate success. Never if it would push stress to 5.

**This is a GM decision.** Don't ask permission — narrate the success, let the complication land, update stress.

## Oracle & NPC Behavior

NPCs have their own goals and motivations. Oracle informs circumstances, not character.

> Full system: `references/oracle-guide.md` — NPC agency, priming, interpretation, examples

## Player Agency

- Present situations, not solutions
- Honor player choices even when suboptimal
- The story belongs to the character, not the plot

## Pressure Clocks

Clocks make pressure visible and force the GM to honor it. Stored as JSON in `clocks.json` (campaign folder), managed via `scripts/clocks.py`. Three default scopes:

- **Tactical (4 segments)** — scene-level pressure (guards converging, fire spreading)
- **Encounter (6 segments)** — single arc (heist discovered, ally's patience)
- **Campaign (8 segments)** — long horizon (war approaches, secret revealed)

**Surface protocol:** name the clock when you create it; show state at scene transitions and when an encounter starts; announce ticks. Hidden pressure goes in `gm-notes.md`, not on a clock.

**Tick triggers:** partial successes, bane elaborations on relevant oracles, time skips, scene transitions, narrative beats. Each tick needs a stated reason (logged in the audit trail).

**On completion:** the clock archives with a resolution narrative + step history, so the consequence sequence is preserved for callbacks.

> Full guide: `references/clocks.md`

## Time Skips

When time needs to pass — travel, recovery, between arcs — roll oracle for active threads, update state, narrate the summary.

> Full procedure: `references/time-skips.md`

## Pacing

- Match the writing guide's tone
- Vary scene length — not every moment needs equal weight
- End responses at decision points, not mid-action
