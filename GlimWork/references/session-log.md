# Session Log

A persistent file (`session-log.md`) that accumulates across sessions. Unlike `current.md` which captures current state, the session log is a running history.

---

## Format

```markdown
# Session Log — [Campaign Name]

---

### Chapter X, Session Y
[2-4 lines: Key beats, turning points, emotional moments. 
No mechanics — just what would jog memory months later.]

### Chapter X, Session Y-1
[Previous session...]
```

---

## Purpose

- Quick reference when resuming after a long break
- Helps GM maintain continuity across context resets
- Player can review their character's journey at a glance

---

## Style Guidelines

- **Newest entries at top**
- Fragment sentences are fine — scannable > polished
- Focus on: decisions made, relationships changed, revelations, consequences
- Omit: routine travel, minor combat, mechanical details

---

## When to Write

- At Session End, before repacking the .glim
- Summarize in one breath: "What would I tell someone who asked what happened?"

---

## Searching the Log

For long-running campaigns, use `log_search.py` to find relevant history without loading the entire file:

```bash
# Find all entries mentioning a character
python scripts/log_search.py session-log.md "Isolde"

# Regex patterns work — find dragons or wyrms
python scripts/log_search.py session-log.md "dragon|wyrm"

# Find a specific chapter range
python scripts/log_search.py session-log.md "Chapter 1[0-5]"

# Just list matching session headers (quick scan)
python scripts/log_search.py session-log.md "betrayal" --headers-only
```

Returns complete session entries (not lines), preserving context.

**Use when:**
- Player asks "when did we meet [NPC]?" or "what happened with [plot thread]?"
- You need to recall consequences of past decisions
- Checking continuity before introducing callbacks

---

## Example

```markdown
# Session Log — Glim's Journey

---

### Chapter 15, Session 2
Cira intervention on frozen plateau. Glim's breakdown. Isolde reconciliation 
in the mountain lair. Return to Dragonmeet; Aldric's family visit. 
Accountability discussion — agreed to meet caravan survivors, infrastructure service.

### Chapter 15, Session 1
Nine months of wandering. Apex growth. Rockslide incident (6 survivors). 
The Echo's question in the Sundered Reaches: "What do you want to be remembered for?"

### Chapter 14, Session 3
Final confrontation with the Wyrm cult. Betrayal by Marcus — he was a sleeper agent.
Isolde wounded protecting Glim. Dragon fire in the temple ruins.
```

