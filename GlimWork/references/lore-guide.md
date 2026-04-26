# Lore Files — Guidance

How and when to create persistent lore documents during campaign play.

---

## Purpose

Lore files store world information that:
- Is too detailed to fit in the main save file
- Gets referenced repeatedly across sessions
- Represents knowledge the *player* needs accessible (not just the character)
- Would clutter session flow if explained every time

---

## When to Create a Lore File

**Create a new lore file when:**

1. **A system emerges that needs tracking**
   - Magic systems with specific rules
   - Political structures with many factions
   - Custom mechanics unique to this campaign
   
2. **The world expands significantly**
   - New regions with their own cultures, powers, conflicts
   - International relations beyond the starting area
   - Historical revelations that reframe everything

3. **Information keeps getting repeated**
   - If you're explaining the same thing every few sessions, document it
   
4. **Complexity exceeds save file scope**
   - The main save should be a quick reference
   - Deep dives belong in lore files

---

## Standard Lore File Types

### `world.md` — Geography & Politics
- Major powers and their relationships
- Regional cultures and conflicts  
- Trade routes, borders, tensions
- International situation

### `history.md` — What Came Before
- Timeline of significant events
- Hidden truths about the past
- How history shapes the present
- What different factions believe vs. what's true

### `factions.md` — Organizations & Groups
- Major players beyond individual NPCs
- Their goals, methods, resources
- Internal divisions and politics
- Relationships to each other

### `magic.md` — Supernatural Systems
- How magic/powers work in this world
- Limitations and costs
- Different traditions or approaches
- What the characters know vs. hidden rules

### `[custom].md` — Campaign-Specific
- Whatever this particular story needs
- Named for what it tracks

---

## Example — Glim Campaign Lore Files

| File | Purpose |
|------|---------|
| `glim_world_international.md` | The five neighboring powers, their magical paradigms, political stances, and how they view the kingdom's transformation |
| `glim_growth_system.md` | Dragon size progression, triggers, philosophy, mechanical effects |
| `glim_campaign_notes.md` | Meta-level GM guidance—lessons learned, pacing notes, NPC behavior reminders |

---

## Lore File Structure

```markdown
# [Topic] — [Campaign Name]

Brief description of what this file covers.

---

## [Major Section]

### [Subsection]
Content here.

### [Subsection]
Content here.

---

## [Major Section]

...

---

## Implications for Play

[How this lore affects the campaign—hooks, tensions, questions]

---

*Last updated: [Chapter/Date]*
```

---

## Maintaining Lore Files

### During Play
- Note when new information should be added
- Flag contradictions for resolution
- Mark sections as [OUTDATED] if events have changed them

### Between Sessions
- Update with new revelations
- Remove or archive obsolete information
- Add "Implications for Play" notes

### Version Control
- Date your updates
- Consider keeping old versions in `lore/archive/` for campaign history

---

## Integration with Save Files

The main save file (`current.md`) should:
- Summarize key points from lore files
- Reference lore files for deep dives: *"See `world.md` for full international details"*
- Not duplicate extensive lore content

The lore files should:
- Stand alone as reference documents
- Not require reading the save file to understand
- Be searchable for specific topics

---

## When NOT to Create a Lore File

- One-off details that won't recur
- Information that fits naturally in the save file
- Speculation or possibilities (keep in session notes instead)
- Anything the character doesn't know and won't learn

**Rule of thumb:** If you won't reference it again, it doesn't need a file.

---

*Template version 1.0*