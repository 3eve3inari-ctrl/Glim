# Time Skips & Montages

Narrative tools for compressing time while maintaining story momentum and character continuity.

---

## When to Use

**Time skips** work well when:
- The interesting part is what comes *after*, not during
- Multiple threads need to resolve offscreen
- The character needs recovery time (stress, wounds, resources)
- The story needs a tonal reset or new chapter feeling
- Travel or waiting would be tedious to play moment-by-moment

**Offer a skip when:**
- A major arc concludes and the next hasn't begun
- The player says "I want to lay low for a while"
- Narrative logic demands passage of time ("The ship takes three weeks to arrive")

---

## Types of Skips

### Short Montage (hours to days)
- "The night passes" / "You make camp and rest"
- Usually no oracle rolls needed
- Brief narration, then resume
- Good for: recovery, travel between nearby locations, waiting for an event

### Medium Skip (days to weeks)
- "A week of preparation" / "The journey north"
- Oracle rolls for 1-3 key threads
- Player input: "What do you focus on during this time?"
- Good for: travel, training, investigation, laying low

### Long Time Jump (months to years)
- "Six months later..." / "When spring comes..."
- Oracle rolls for all active threads
- Significant state changes possible
- May warrant advancement
- Good for: between major story arcs, after transformative events

---

## The Procedure

### 1. Establish Scope
Confirm with the player:
> "Ready to skip ahead? How long are we talking — days, weeks, months?"

Or propose based on fiction:
> "The journey to the capital takes about two weeks. Want to skip ahead, or play out moments on the road?"

### 2. Identify Threads
List the active threads that could change during the skip:
- Open plot questions
- NPC situations
- Pending consequences
- World events in motion

### 3. Player Input
Ask what the character does with their time:
> "What's [character] focusing on during these weeks?"

This might affect:
- Which threads matter most
- Potential skill improvement
- Stress recovery
- New contacts or resources

### 4. Roll the Oracle
For each relevant thread, roll the three-die oracle. Set likelihood per thread based on how plausible the answer is — don't default everything to fifty-fifty.

```bash
python scripts/dice.py oracle-batch --likelihood likely "Did Renn deliver?" "Patrol noticed?" "Council convened?"
```

Per-thread likelihood:

```bash
python scripts/dice.py oracle-batch "Letter arrived:very_likely" "Patrol noticed:unlikely" "Council convened:fifty_fifty"
```

Each thread produces a composed result from Die 1 (yes/no), Die 2 (elaboration), Die 3 (boon/bane):

| Result | Meaning |
|--------|---------|
| Yes, and... | It happens, and there's more |
| Yes | It happens |
| Yes, but... | It happens, with a cost |
| No, but... | Doesn't happen, but there's a silver lining |
| No | Doesn't happen |
| No, and... | Doesn't happen, and there's a deeper consequence |

**Roll first, interpret second.** Don't decide what you want to happen — let the dice create the situation, then narrate backward. The d10 boon/bane is what keeps this honest.

See `oracle-guide.md` for full mechanics.

### 5. Update State
After rolling:
- **Stress**: Typically clears 1-2 for short skips, potentially all for long skips with safe rest
- **Story Points**: Only reset on advancement, not time passage
- **Resources**: May change based on fiction (spent money, acquired gear)
- **Relationships**: Oracle results may shift NPC attitudes

### 6. Narrate the Summary
Weave the oracle results into a cohesive summary. You can:
- Present all results at once (efficient)
- Reveal dramatically one by one (suspenseful)
- Frame as memories or reports the character receives

### 7. Offer the Landing
End with a concrete moment:
> "It's been three months. You're [location], and [immediate situation]. What do you do?"

Give the player something to respond to, not just exposition.

---

## Player Involvement

### Active Skips
The player can influence the skip:
- "I spend the time training my swordsmanship"
- "I'm trying to track down information about [thread]"
- "I want to build a relationship with [NPC]"

This might grant advantage on relevant oracle rolls or inform what threads matter.

### Passive Skips
Sometimes the player just wants time to pass:
- "I lay low and recover"
- "Just skip to when the letter arrives"

That's fine — run the oracles, narrate the summary, move on.

---

## Examples

### Short: Recovery Night
> **GM**: "You make it back to the safehouse. Night passes — recover 1 stress. Morning comes with rain against the windows. What's the plan?"

No oracle needed. Simple transition.

### Medium: Two Weeks of Investigation
> **Player**: "I want to spend time digging into the Vance family history."
> 
> **GM**: "Two weeks of research. Let me roll for a few threads..."
> - Does the investigation turn up anything useful? → Oracle: 4 (Yes, but...)
> - Does anyone notice you asking questions? → Oracle: 5 (Yes)
> 
> **GM**: "You find what you're looking for — birth records that don't add up, a sealed inheritance dispute. But someone's noticed your interest. A clerk at the archive mentioned you to the wrong person. You've got the information, but you're not the only one who knows you have it."

### Long: Six Month Time Jump
> **GM**: "Six months pass. Let's see what the world's been doing..."
> 
> *[Rolls for 8 threads, records results]*
> 
> **GM**: "The good news: Aldric's rule has stabilized, the northern border is holding, and Isolde's recovery went better than anyone hoped. The bad news: Storms-End didn't make it — complications, the Windsworn are in chaos. And there's something else: ships from across the ocean have been sighted. They're not attacking. They want to talk.
>
> It's early spring. You're at the Dragonmeet, and a royal messenger just arrived with a sealed letter. What do you do?"

---

## Tips

- **Don't skip conflict** — If something dramatic is happening, play it out
- **Skips create momentum** — Use them to propel the story forward, not avoid it
- **Oracle results are prompts** — "No, and..." doesn't mean nothing happens; it means something worse does
- **Let players veto** — If they want to play out the journey, let them
- **Save before long skips** — Multiple oracle rolls can shift the story significantly

---

*Time is a story tool. Compress it when it serves the narrative; expand it when the moments matter.*

