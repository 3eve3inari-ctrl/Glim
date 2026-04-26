# Context Management Guide

Files load into context. Keep core files lean; load lore dynamically.

---

## Loading Tiers

| Tier | Files | When to Load |
|------|-------|--------------|
| **Always** | `character-sheet.md`, `current.md`, `gm-notes.md`, `writing-guide.md`, `oracle-guide.md` | Every session start |
| **Dynamic** | `lore/*` dossiers | When NPC/location/faction appears in scene |
| **Session End** | `advancement.md` | When discussing advancement at session conclusion |
| **Never** | `session-log.md` | Search via `log_search.py`, never load wholesale |

---

## Length Targets

| File | Target | Pruning Rule |
|------|--------|--------------|
| `character-sheet.md` | ~150 lines | Summarize old discoveries; keep actionable secrets |
| `current.md` | ~100 lines | Resolved threads → session-log; only active state |
| `gm-notes.md` | ~100 lines | Extract details to lore; keep only active machinery |
| Dossiers (full) | 150-250 words | One file per NPC/location/org |
| Dossiers (background) | 50-75 words | Texture only |

---

## gm-notes.md vs Lore Files

**gm-notes.md** is for *active plot machinery*:
- Plot threads and their intended direction
- NPC secrets the PC hasn't discovered
- Seeds planted but not yet paid off
- Offscreen events in motion
- GM reminders for this arc

**Lore files** are for *reference material*:
- NPC personality, history, relationships, appearance
- Location atmosphere, layout, inhabitants
- Faction goals, resources, structure
- World rules, history, customs

**The test:** If it's about *what the thing IS*, put it in lore. If it's about *what the GM is planning to do with it*, put it in gm-notes.

**When to extract:** If gm-notes has detailed NPC psychology, location descriptions, or faction structures—move those to lore dossiers. Keep gm-notes focused on *secrets and intentions*.

---

## Dynamic Lore Loading

Don't load all lore at session start. Load when relevant:

| Trigger | Load |
|---------|------|
| NPC appears in scene | Their dossier from `lore/characters/` or `lore/background/` |
| PC enters location | Location dossier from `lore/locations/` |
| Faction becomes relevant | Organization dossier from `lore/organizations/` |
| Setting detail matters | Relevant file from `lore/world/` |
| History question arises | Search `session-log.md` via `log_search.py` |

---

## What to Prune

**current.md:**
- Resolved threads → move summary to session-log.md
- Session summary → lives in session-log, not current
- Mechanical notes that duplicate character-sheet → remove
- NPCs no longer active → remove from Key NPCs (dossier persists)

**gm-notes.md:**
- Seeds that paid off → remove
- Resolved plot threads → remove
- NPC details → extract to lore dossier
- Location details → extract to lore dossier
- Arc structures after arc completes → remove

**character-sheet.md:**
- Old discoveries that are now common knowledge → summarize
- Contacts who became Key NPCs → reference dossier instead

---

*Keep always-loaded files lean. Load details on demand. Prune aggressively at session end.*

