# Oracle Guide

The oracle resolves uncertainty about the world — things the GM genuinely doesn't know. It fills narrative gaps, not generates chaos.

The oracle is **three dice**, rolled together:

| Die | Sides | Determines |
|-----|-------|------------|
| **Die 1** | d6 | Yes/no, with a likelihood-weighted threshold |
| **Die 2** | d6 | Elaboration — `but` / plain / `and` |
| **Die 3** | d10 | Boon (10) / Bane (1) / neutral (2-9) — promotes Die 2 |

Always roll all three. The d10 is the keystone — it's why the oracle bites instead of drifting toward whatever feels nice in the moment.

---

## Why Three Dice

The single-d6 oracle assumed every question was 50/50. It isn't. *"Does the council already know?"* and *"Is the shop open at 3 a.m.?"* are not the same shape of uncertainty. Die 1 lets the GM weight the question honestly.

But weighting alone has a failure mode: when the GM sets the likelihood, they can quietly skew toward the answer they want. Die 3 — the boon/bane — exists to break that. **It's always rolled, and 20% of the time it forces a complication or a windfall the GM didn't choose.** Mechanism over mood. The GM can be honest about likelihood *because* fate still has its hand in.

This matters specifically for an LLM GM, which tends toward agreeable narration. The d10 makes "less kind" mechanically inevitable, not a discipline the GM has to remember. The goal isn't to punish — it's to introduce challenges the player feels rewarded for overcoming.

---

## Die 1 — Likelihood (yes/no)

The GM declares a likelihood *before* rolling. This sets the threshold on a d6.

| Likelihood | Yes on | Yes % | When |
|------------|--------|-------|------|
| Sure thing | auto-yes | 100% | Almost certain — but you want fate to weigh in via Die 2/3 |
| Very likely | 2-6 | ~83% | Strongly favored by circumstance |
| Likely | 3-6 | ~67% | Tilted in favor |
| Fifty-fifty | 4-6 | 50% | Genuine uncertainty (default) |
| Unlikely | 5-6 | ~33% | Tilted against |
| Very unlikely | 6 | ~17% | Strongly disfavored |
| Impossible | auto-no | 0% | Almost certainly not — but Die 2/3 still flavor the no |

**Setting likelihood is a GM judgment, not a player negotiation.** Be honest about the world. If the question's answer is genuinely 70/30, set "likely" — don't slide to fifty-fifty because you'd prefer either outcome equally.

---

## Die 2 — Elaboration

An independent d6, mapped to three slots:

| Roll | Elaboration | What it adds |
|------|-------------|--------------|
| 1-2 | **but** | Complication — the answer comes with a twist or cost |
| 3-4 | plain | No elaboration — the answer stands as-is |
| 5-6 | **and** | Extension — the answer reveals more in the same direction |

Elaboration is **direction-agnostic**. "And" extends whatever direction Die 1 gave; "but" softens it.

| Composed result | What it means |
|-----------------|---------------|
| Yes, and... | It happens, plus something more (extension of the affirmative) |
| Yes | It happens, neutrally |
| Yes, but... | It happens, but with a cost or complication |
| No, but... | It doesn't happen, but there's a silver lining |
| No | It doesn't happen, neutrally |
| No, and... | It doesn't happen, and the answer reveals more (extension of the negative) |

---

## Die 3 — Boon / Bane

A d10. **Always rolled.**

| Roll | Effect |
|------|--------|
| 1 | **Bane** — promote Die 2 one step toward unfavorable for the PC |
| 2-9 | Neutral — Die 2 stands |
| 10 | **Boon** — promote Die 2 one step toward favorable for the PC |

**Promote one step on a PC-favorability scale:**

- On a **Yes** result: `but → plain → and` is the favorability ladder. (Yes,and is best; Yes,but is worst.)
- On a **No** result: `and → plain → but` is the favorability ladder. (No,but is best — silver lining; No,and is worst — extension of bad news.)

So:
- Boon on `Yes, but` → `Yes` (better yes for PC)
- Boon on `Yes` → `Yes, and` (best yes for PC)
- Boon on `Yes, and` → no-op (already maxed)
- Boon on `No, and` → `No` (less bad)
- Boon on `No` → `No, but` (silver lining)
- Boon on `No, but` → no-op (already maxed favorable)
- Bane mirrors in reverse — softens favorable, sharpens unfavorable.

**Direction never flips.** A Yes stays a Yes; a No stays a No. Boon/bane only modulates the elaboration's flavor, not the answer.

### Why "boon" and "bane" instead of "and"/"but"?

Die 2 already produces `and`/`but` as base elaborations — those are *texture*, not luck. Die 3 is a *modifier* on top, expressing whether fate leans toward or against the PC on this particular roll. They're separate axes:

- **Die 2** asks: how much does the answer reveal?
- **Die 3** asks: did the dice break for the PC or against?

A Yes,and from a clean Die 2 with neutral Die 3 is "yes, with extension." A Yes,and that came from a Yes,plain promoted by a boon is "yes... and *fate threw in something extra in your favor*." Mechanically identical, narratively the same, but the audit trail tells you whether the universe was generous or merely thorough.

---

## NPC Agency

**NPCs have their own goals, priorities, and motivations.** These persist regardless of oracle rolls.

Oracle informs *circumstances*, not *character*:
- A traitor doesn't become loyal on a good roll — they might be in a good mood, or distracted, or see an opportunity
- A loyal ally doesn't betray the PC on a bad roll — they might be busy, or misinformed, or unable to help right now
- The oracle tells you about timing, mood, external factors — not whether an NPC is suddenly someone different

**The NPC's established nature is fixed.** Oracle reveals how that nature manifests *in this moment*.

---

## When to Roll

Use the oracle for **meaningful uncertainty** — questions where the answer matters and isn't already established.

### Offscreen Actions
What happened while the PC wasn't watching?
- Did the messenger deliver the warning? (likely)
- Did Renn follow through on his plan? (depends on his disposition — likely or unlikely)
- Has the council already made their decision? (fifty-fifty if no clock; otherwise read the clock)

*Roll at session start or when the PC would learn the answer.*

### NPC Disposition
How is an NPC primed before an interaction begins?
- Is the captain in a good mood today? (fifty-fifty unless something happened)
- Does the contact trust us after last time? (likely if we delivered; unlikely if we didn't)
- Is the shopkeeper suspicious of strangers? (depends on the city)

*Roll before the scene, then play the NPC consistently with that result.*

### Unestablished World State
Facts about the world that haven't been determined:
- Is the shop open at this hour? (depends on hour — set likelihood honestly)
- Did it rain last night? (fifty-fifty in spring, unlikely in summer)
- Is there a back entrance? (likely for most buildings, unlikely for a vault)

*Roll when the PC would reasonably discover the answer.*

### Ambiguous Consequences
When an action's ripple effects are unclear:
- Does the noise carry to the guards? (depends on stealth + distance)
- Does the fire spread to the next building? (likely if dry, unlikely if damp)
- Did anyone see us leave together? (depends on crowd density)

*Roll when the consequence becomes relevant, not preemptively.*

---

## When NOT to Roll

### Player Actions
If the PC is *doing* something, that's a skill roll, not an oracle question.
- "Do I pick the lock?" → Skill roll
- "Is the lock pickable?" → Oracle

### Already Established Fiction
If you've already said it, don't contradict it with a roll.
- The captain was friendly last scene → Still friendly (unless something changed)

### NPC Behavior Mid-Scene
NPCs have motivations. Play them consistently.
- Don't roll to see if an NPC suddenly changes their mind
- Roll *before* the scene to set disposition, then honor it

### Constant Surveillance
Avoid paranoia-inducing questions:
- "Is anyone watching right now?"
- "Did someone notice that?"

Roll for consequences when they matter — not as constant background threat.

### Meaningless Questions
If the answer doesn't change anything, don't roll. Narrate instead.

---

## Internal States (Optional)

The oracle can reveal character psychology when:
- The answer isn't obvious from established characterization
- The GM deciding feels like overreach into player domain
- The player rolling feels too mechanical for an emotional beat
- The tension between "want" and "do" is interesting

**Examples:**
- "Does she enjoy this more than she expected?" (fifty-fifty — let fate speak)
- "Is the dragon-part satisfied, or does it want more?" (likelihood depends on what just happened)
- "Does he feel guilt, or has he rationalized it?" (likely if he's aware; unlikely if he's not)

**Why it works:** The oracle externalizes ambiguity. The player discovers their character rather than dictating them. A "No, but..." on "does she enjoy the killing" creates a different character moment than a flat "Yes" — and neither the GM nor the player had to decide. The dice revealed it.

**Don't use when:**
- The player has established the internal state through narration
- It would undercut player agency on an active choice
- The answer is already obvious from context

---

## NPC Priming Example (with three dice)

**Setup:** The player wants to convince a guard captain to let them into the restricted archives.

---

**Step 1: Player declares intent**
> "I approach Captain Voss and try to persuade her that I have legitimate scholarly business in the archives."

**Step 2: GM sets likelihood and rolls**

The GM judges Voss's mood honestly: there's been a recent breach, she's stressed, scholars are normally welcome but tonight is different. Set to **unlikely** (yes on 5-6).

```bash
python scripts/dice.py oracle unlikely
```

> Die 1: 4 (no — below threshold of 5)
> Die 2: 6 (and — extension)
> Die 3: 1 (bane)
>
> Bane on No,and is a no-op (already most unfavorable for PC). Final: **No, and...**

**Step 3: GM interprets**

Voss isn't receptive — and there's more. She's not just busy; she's actively suspicious of any outside inquiries right now. The bane locked in the worst-case elaboration. DC for any Persuasion roll bumps to Difficult (18); Voss may also call in backup if pushed.

**Step 4: Scene unfolds**
> GM: "Captain Voss looks up from a sheaf of reports. 'The archives are closed,' she says — flatly. Her hand isn't on her blade, but it's nearby. Behind her, you notice another guard quietly stepping back into the corridor. The conversation hasn't started, but reinforcements are already being summoned."

**Step 5: Player decides**

The player knows this is bad. They can press (DC 18, with consequences) or retreat (and look for another way in). The oracle shaped the scene; the player still chooses the action.

---

**How a different Die 3 would have changed it:**

Same Die 1 (4) and Die 2 (6) — but Die 3 = 10 (boon).

Boon on No,and → No (one step toward favorable). Voss still refuses, but it's a flat refusal — no extra suspicion, no backup, just a closed door. DC for a re-approach later might still be Challenging (14), but the scene doesn't escalate.

That's the d10 doing its job: same likelihood, same elaboration roll, but fate broke differently.

---

## Interpreting Results

### No, and... (No + Extension, often hardened by bane)
> *"Did the letter arrive in time?"*
> No, and... the messenger was intercepted. Someone else has read it.

### No
> *"Is the shop still open?"*
> No — the shutters are closed, the owner gone for the night.

### No, but... (No + Silver Lining, often softened by boon)
> *"Does the guard believe my cover story?"*
> No, but... he's too tired to make trouble. He waves you through.

### Yes, but... (Yes + Complication, often softened from Yes by bane)
> *"Did Renn deliver the package as promised?"*
> Yes, but... he was seen. Someone's asking questions.

### Yes
> *"Is the informant at the usual meeting spot?"*
> Yes — she's there, waiting in the corner booth.

### Yes, and... (Yes + Extension, often hardened by boon)
> *"Did the storm pass overnight?"*
> Yes, and... it washed away the tracks. Your pursuers lost the trail.

---

## Reading the Audit Trail

The script's `breakdown` field tells you which dice produced the result:

```
Die1 4 (no, unlikely) | Die2 6 (and) | Die3 1 (bane) → No, and...
```

This means: the GM set the question as unlikely, the d6 came in below threshold (no), elaboration rolled an "and" (extension), and the d10 came up bane (which would push toward unfavorable, but No,and is already maxed there — no-op).

Reading the trail makes it clear *why* a result feels heavy: was it baseline likelihood, an unlucky elaboration, or fate piling on? Useful for narration.

---

## Time Skips

When time passes, roll for multiple threads at once:

```bash
python scripts/dice.py oracle-batch --likelihood likely "Did Renn deliver?" "Is the council in session?" "Has the patrol noticed?"
```

Per-thread likelihood with `name:likelihood` syntax:

```bash
python scripts/dice.py oracle-batch "Letter arrived:very_likely" "Patrol noticed:unlikely"
```

See `references/time-skips.md` for the full procedure.

---

*The oracle reveals what you don't know. It doesn't override what you do.*

*Likelihood is GM judgment about the world. Boon/bane is fate's veto. Together they keep the GM honest.*
