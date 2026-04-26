# Campaign Interview Guide

## Purpose
Establish character, world, tone, and player preferences before play begins.
Output: Initial save file + writing-guide.md + starter lore docs.

---

## Phase 0: Entry Point

**Open with:**
> "What are we playing? A few options:
> - An **original world** of your own
> - An **existing setting** (Harry Potter, Marvel, Star Wars, etc.)
> - A **mashup** of two settings
> - The **default Glim setting** — a frontier-survival low-fantasy world that's becoming high-fantasy as magic, monsters, and dungeons appear. Useful jumping-off point if you don't have a world in mind."

**Branch based on answer:**

### Path A: Established Setting
> "Perfect — I know [setting]. A few quick questions:"
> 
> 1. "When and where in that world? Which era, which corner?"
> 2. "Who are you in it? Role, allegiance, situation?"
> 3. "What interests you that the source didn't fully explore?"
> 4. "Faithful to canon tone, or shifted? (Darker? Lighter? Weirder?)"
> 5. "Any canon characters you want involved, or original cast only?"

Then skip to Phase 4 (Themes), Phase 5 (Fun), Phase 6 (Boundaries).

Generate lore docs as "reference sheets" — key facts, timeline placement, 
relevant canon characters, with a note that we're playing in borrowed space.

### Path B: Original World
Proceed with full interview (Phases 1-6).

### Path C: Hybrid
> "So [base setting] but with [twist]. Let me confirm what's kept 
> and what's changed..."

Map the delta from canon, then proceed as Path A.

### Path D: Default Glim Setting

The default setting is a low-fantasy world (flint-and-steel tech) where, ~25 years ago, magic, monsters, and dungeons began appearing in the lands west of the homeland. The PC is part of a chartered expedition into this new territory, which is held by sapient natives (the Vahn) whose magic is shape-binding and whose relationship with the new monsters is fundamentally different from the settlers'. Tone: frontier survival, awe and dread at the magical, colonial moral weight.

**Setup procedure:**

1. **Confirm the setting choice.** Briefly pitch:
   > "It's a frontier-survival setting where you're a charter settler in lands held by indigenous shapeshifters called the Vahn. Magic is new, dangerous, and self-taught. Monsters are real and often tragic. The colonial tension is the moral spine. Sound right?"

2. **Copy the world layer** from `Examples/Glim-Default/lore/` into the new campaign folder's `lore/` directory:
   - `world/the-glim.md`
   - `world/the-vahn.md`
   - `locations/lantern-hold.md`
   - `characters/captain-rhel-daven.md`

3. **Skip Phase 3 (World)** — the world is set. Run a brief Phase 1 (character pitch) and Phase 2 (character mechanics), tailored to the Glim setting:
   > "You're at Lantern Hold, a six-month-old palisade settlement on land the bear-line of the Vahn previously used for summer gathering. You report to Captain Rhel Daven. Tell me about your character — who they are, what brought them on the charter, what they're good at."

4. **Suggest starting roles** if the player needs a prompt:
   - **Scout/ranger** — eyes for the expedition; often alone in the wild
   - **Hedge mage** — self-taught Glim practitioner; high risk, high curiosity
   - **Hired blade** — bodyguard or monster-hunter; the captain's enforcer
   - **Settler with a craft** (smith, healer, surveyor) — civilian-perspective; domestic stakes
   - **Scholar / cartographer** — driven by curiosity; might apprentice to Kenric Maul

5. **Proceed to Phase 4 (Themes), Phase 5 (Fun), Phase 6 (Boundaries).** The setting's tone is already established in `Examples/Glim-Default/writing-guide.md` — copy and adapt rather than starting from scratch.

6. **Starting situation:** The PC arrives at Lantern Hold (or has been there a few weeks). Captain Daven will assess them in the first scene. Bren — a scout — disappeared four nights before the PC's arrival. The bear-line has not visited the wall since their second formal meeting six weeks ago. Use these as opening hooks.

7. **Reference the example campaign** (`Examples/Glim-Default/`) for a worked example of how the setting plays — including a session-log demonstrating the new oracle and clock mechanics in use.

---

## Phase 1: The Hook

**Open with:**
> "What's the elevator pitch? Who do you want to play, and what kind of world do they live in?"

Let them dump whatever they have. Could be:
- A full concept ("exiled dragon princess in a low-magic kingdom")
- A vibe ("cyberpunk noir, solo thief")
- A fragment ("I want to play a healer who's lost their faith")

**If sparse, prompt:**
- "What genre or setting pulls you right now?"
- "Any characters from fiction you want to echo?"
- "What's one scene you'd love to play?"

---

## Phase 2: Character

**Core questions:**
- "What are they good at? What are they bad at?"
- "What do they want — surface level and deeper?"
- "What's their flaw or tension?"
- "How do others see them vs. how they see themselves?"

**Mechanical translation:**
- Map answers to stat spread (Physical/Technical/Social)
- Identify 5 starting proficiencies from their concept
- Note any genre-specific features (cyberware, magic, mutations)

---

## Phase 3: World

**Core questions:**
- "What's the state of the world — stable, crumbling, at war, rebuilding?"
- "Who holds power? Who's powerless?"
- "What's the supernatural/technological situation?"
- "What's the scale — street-level, kingdom-wide, continental, cosmic?"

**If they have existing lore:** Ask for documents, integrate.
**If building fresh:** Sketch together, leave gaps for discovery.

---

## Phase 4: Themes & Tone

**Core questions:**
- "What do you want to explore? What questions interest you?"
- "What's the emotional register — gritty, hopeful, tragic, adventurous, mixed?"
- "Any subjects to avoid or handle carefully?"

**Style questions:**
- "Short punchy prose or longer lyrical passages?"
- "How much mechanical detail in narration?"
- "Action-heavy, intrigue-heavy, relationship-heavy, or balanced?"

---

## Phase 5: Fun Sources

**Core questions:**
- "What makes a session feel good to you?"
- "Combat? Heists? Politics? Exploration? Relationships? Building things?"
- "Do you like being challenged mechanically, narratively, or both?"
- "How much do you want me to drive vs. wait for your lead?"

---

## Phase 6: Boundaries

**Ask directly:**
- "Anything off-limits — topics, tones, content?"
- "Anything you want handled carefully, with a heads-up before it appears?"

Note these in writing-guide.md for persistent reference.

---

## Output Checklist

After interview, generate:
- [ ] `current.md` — Initial save with character sheet, starter threads, empty session log
- [ ] `writing-guide.md` — Tone, themes, pacing, boundaries, style notes
- [ ] `lore/` — Starter world docs based on what was established
- [ ] Pack as `[campaign-name].glim`