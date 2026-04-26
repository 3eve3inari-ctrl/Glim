# Clocks

Clocks are the GM's pacing instrument. They make pressure visible, give time stakes, and turn "this is getting worse" into segments the player can see filling. Use them to track progress across scales — a single conversation, a heist arc, or a kingdom-spanning faction goal.

Clocks live as JSON in `clocks.json` (in the campaign folder, alongside `current.md` and `gm-notes.md`). Manage them with `scripts/clocks.py`.

---

## Sizes by Scope

| Scope | Default Size | Use For |
|-------|--------------|---------|
| **tactical** | 4 segments | Scene-level pressure — guards converging, fire spreading, a conversation going south |
| **encounter** | 6 segments | A single arc — heist discovered, ally's patience, faction suspicion in a city |
| **campaign** | 8 segments | Long horizon — war approaches, a secret is uncovered, the kingdom's collapse |

Sizes are defaults; override when the fiction wants more or fewer beats. Don't pad — a 4-segment tactical clock fills fast, which is the point.

---

## When to Create a Clock

Make one explicit when:

- An **encounter starts** (combat or social) and there's pressure beyond the immediate roll
- A **threat has a horizon** but isn't immediate (the council is meeting, the army marches)
- The PC starts a **multi-step undertaking** with risk of being interrupted (research, infiltration, negotiation)
- An offscreen **clock would otherwise be invisible** to the player — making it explicit creates real time pressure

If the situation just resolves with a single roll, no clock needed. Clocks are for things that take *beats* to resolve.

---

## Fill Triggers

Fill segments when:

- A **roll partially succeeds** at a clock-relevant action — narrate the cost as a tick
- A **bane elaboration** lands on a clock-relevant oracle — fate accelerates the threat
- A **scene transition** passes time the clock cares about
- A **time skip** advances all relevant clocks (use `--trigger "time skip"`)
- The PC **chooses to delay** when the clock is ticking
- A **narrative beat** logically advances things ("the courier reaches the capital")

Don't tick clocks because nothing happened. Each tick should have a stated reason — that's why `--trigger` is required in the audit log.

---

## Surface Protocol

The clock's mechanical effect comes from being *seen*. The GM should:

1. **Name the clock when you create it** — out loud to the player. "There's now a 6-segment clock: the Heist Is Discovered."
2. **Show state at scene transitions** — current fill, what would tick it next.
3. **Show state when an encounter starts** — relevant clocks become visible at the top of the scene.
4. **Announce ticks** — when a segment fills, narrate it. The fill is the consequence.
5. **Re-surface dormant clocks** when they become relevant — "Remember the Council clock? It's at 4/6 now."

A hidden clock is fine for GM notes (use `gm-notes.md` instead). A *Pressure Clock* is a contract with the player: this is happening, and you can see it coming.

---

## Completion

When a clock fills, the threat *lands* — the council decides, the heist is blown, the army arrives. Resolve the consequence in fiction, then archive it with `complete --resolution "narrative"`.

The archive captures:

- The **challenge** (name, scope, size)
- The **resolution narrative** — what actually happened when it landed
- The **step history** — every tick with its trigger

This becomes a record of how the PC dealt (or didn't deal) with each pressure. Useful for session-log condensation and for callbacks later.

A filled clock doesn't *have* to mean disaster — it just means the situation has matured. The resolution narrative is where the GM lands the consequence in proportion to the fiction.

---

## Schema

`clocks.json` structure:

```json
{
  "active": {
    "council-decides": {
      "name": "Council decides on petition",
      "size": 6,
      "filled": 3,
      "scope": "encounter",
      "created": "2026-04-25",
      "steps": [
        {"date": "2026-04-25", "delta": 2, "trigger": "missed the morning session"},
        {"date": "2026-04-25", "delta": 1, "trigger": "Voss reported the breach"}
      ]
    }
  },
  "completed": [
    {
      "id": "heist-discovered",
      "name": "The job is blown",
      "size": 6,
      "scope": "encounter",
      "created": "2026-04-22",
      "completed": "2026-04-23",
      "resolution": "Mira escaped through the kitchen vents; Tessler took the heat.",
      "steps": [
        {"date": "2026-04-22", "delta": 1, "trigger": "guard noticed the open door"},
        {"date": "2026-04-23", "delta": 2, "trigger": "alarm triggered"},
        {"date": "2026-04-23", "delta": 3, "trigger": "captain identified the trail"}
      ]
    }
  ]
}
```

Slug ids (e.g., `council-decides`) are stable references for tick/complete commands. Names are human labels.

---

## Commands

```bash
# Create
python scripts/clocks.py campaign/clocks.json create council-decides "Council decides on petition" 6 encounter

# Show all active and recent completed
python scripts/clocks.py campaign/clocks.json list

# Show one clock in full
python scripts/clocks.py campaign/clocks.json show council-decides

# Tick (default delta 1)
python scripts/clocks.py campaign/clocks.json tick council-decides --trigger "missed the morning session"
python scripts/clocks.py campaign/clocks.json tick council-decides 2 --trigger "Voss reported the breach"

# Untick (rare — when player reverses progress)
python scripts/clocks.py campaign/clocks.json untick council-decides --trigger "evidence destroyed"

# Complete (when the clock fills, or when the situation resolves early)
python scripts/clocks.py campaign/clocks.json complete council-decides --resolution "Council ruled against; Voss owes a favor"

# Reopen (rare — undo a premature completion)
python scripts/clocks.py campaign/clocks.json reopen council-decides
```

---

## Integration with `current.md`

`current.md` shows a player-facing snapshot of active clocks. The JSON is the source of truth; the markdown table is a render. Reconcile at session end (or whenever `list` and the table drift).

---

## When NOT to Use a Clock

- **One-shot consequences** — a single roll resolves it; no clock needed.
- **Vague background dread** — if you can't say what fills it, it doesn't belong on a clock. Use `gm-notes.md`.
- **Player paranoia** — don't create a clock the player can't influence; it just becomes a sword over their head.

The clock should always have an obvious answer to: *what would the PC do to slow this down?*

---

*Clocks make pressure honest. The player can see the threat approaching — and the GM can't quietly forget it.*
