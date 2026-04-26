#!/usr/bin/env python3
"""
dice.py - Dice roller for the Glimmer RPG system

Usage:
    python dice.py "1d20+5"                     # Standard roll
    python dice.py "2d20kh1+3"                  # Advantage (keep highest 1)
    python dice.py "2d20kl1-2"                  # Disadvantage (keep lowest 1)
    python dice.py oracle [likelihood]          # Three-die oracle (default likelihood: 50/50)
    python dice.py oracle-batch [--likelihood L] "Thread 1" "Thread 2" ...

Likelihoods (Die 1 yes/no threshold):
    sure_thing      yes on 1-6   (auto-yes; rolled for transparency)
    very_likely     yes on 2-6   (~83%)
    likely          yes on 3-6   (~67%)
    fifty_fifty     yes on 4-6   (50%, default)
    unlikely        yes on 5-6   (~33%)
    very_unlikely   yes on 6     (~17%)
    impossible      never        (auto-no; rolled for transparency)

Three-die oracle:
    Die 1 (d6):  yes/no, threshold set by likelihood
    Die 2 (d6):  elaboration — 1-2 "but", 3-4 plain, 5-6 "and"
    Die 3 (d10): boon/bane — 1 bane, 10 boon, 2-9 neutral (always rolled)

Boon/bane promotes Die 2 one step on a PC-favorability scale:
    On Yes:  but < plain < and   (and is best for PC)
    On No:   and < plain < but   (but is best for PC — silver lining)
    Boon shifts toward favorable; bane toward unfavorable. No-ops at edges.

Output: JSON with roll details
"""

import sys
import json
import random
import re


LIKELIHOOD_THRESHOLDS = {
    "sure_thing": 1,
    "very_likely": 2,
    "likely": 3,
    "fifty_fifty": 4,
    "unlikely": 5,
    "very_unlikely": 6,
    "impossible": 7,  # never met by a d6 → auto-no
}

LIKELIHOOD_ALIASES = {
    "sure": "sure_thing",
    "vl": "very_likely",
    "l": "likely",
    "5050": "fifty_fifty",
    "50/50": "fifty_fifty",
    "even": "fifty_fifty",
    "u": "unlikely",
    "vu": "very_unlikely",
    "imp": "impossible",
}


def normalize_likelihood(value: str) -> str:
    key = value.lower().replace("-", "_").replace(" ", "_")
    key = LIKELIHOOD_ALIASES.get(key, key)
    if key not in LIKELIHOOD_THRESHOLDS:
        valid = ", ".join(LIKELIHOOD_THRESHOLDS.keys())
        raise ValueError(f"Unknown likelihood '{value}'. Valid: {valid}")
    return key


def elaboration_from_die2(roll: int) -> str:
    """Map a d6 roll to elaboration slot."""
    if roll <= 2:
        return "but"
    if roll <= 4:
        return "plain"
    return "and"


def boon_bane_from_die3(roll: int) -> str:
    """Map a d10 roll to boon/bane/neutral."""
    if roll == 1:
        return "bane"
    if roll == 10:
        return "boon"
    return "neutral"


def promote_elaboration(elaboration: str, modifier: str, direction: str) -> str:
    """
    Apply boon/bane to elaboration. Promotion is on PC-favorability:
      Yes: but < plain < and
      No:  and < plain < but
    Boon shifts toward favorable, bane toward unfavorable. No-op at edges.
    """
    if modifier == "neutral":
        return elaboration

    yes_scale = ["but", "plain", "and"]
    no_scale = ["and", "plain", "but"]
    scale = yes_scale if direction == "yes" else no_scale

    idx = scale.index(elaboration)
    if modifier == "boon" and idx < 2:
        return scale[idx + 1]
    if modifier == "bane" and idx > 0:
        return scale[idx - 1]
    return elaboration


def compose_result(direction: str, elaboration: str) -> str:
    if elaboration == "plain":
        return "Yes" if direction == "yes" else "No"
    suffix = ", and..." if elaboration == "and" else ", but..."
    head = "Yes" if direction == "yes" else "No"
    return head + suffix


RESULT_MEANINGS = {
    "Yes, and...": "It happens, and the answer reveals more",
    "Yes": "It happens",
    "Yes, but...": "It happens, but with a cost or catch",
    "No, but...": "Doesn't happen, but there's a silver lining",
    "No": "Simply doesn't happen",
    "No, and...": "It doesn't happen, and the answer reveals more",
}


def roll_oracle(likelihood: str = "fifty_fifty") -> dict:
    """Roll the three-die oracle and return the composed result."""
    likelihood_key = normalize_likelihood(likelihood)
    threshold = LIKELIHOOD_THRESHOLDS[likelihood_key]

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    die3 = random.randint(1, 10)

    direction = "yes" if die1 >= threshold else "no"
    base_elaboration = elaboration_from_die2(die2)
    modifier = boon_bane_from_die3(die3)
    final_elaboration = promote_elaboration(base_elaboration, modifier, direction)

    result = compose_result(direction, final_elaboration)

    return {
        "type": "oracle",
        "likelihood": likelihood_key,
        "threshold": (
            "auto-yes" if threshold <= 1
            else "auto-no" if threshold > 6
            else f"yes on {threshold}" if threshold == 6
            else f"yes on {threshold}-6"
        ),
        "die1": die1,
        "die2": die2,
        "die3": die3,
        "direction": direction,
        "base_elaboration": base_elaboration,
        "modifier": modifier,
        "final_elaboration": final_elaboration,
        "result": result,
        "meaning": RESULT_MEANINGS[result],
        "breakdown": (
            f"Die1 {die1} ({direction}, {likelihood_key}) | "
            f"Die2 {die2} ({base_elaboration}) | "
            f"Die3 {die3} ({modifier})"
            + (f" → {final_elaboration}" if modifier != "neutral" and final_elaboration != base_elaboration else "")
            + f" → {result}"
        ),
    }


def roll_oracle_batch(threads: list[str], likelihood: str = "fifty_fifty") -> dict:
    """
    Roll the oracle for multiple threads at once.
    Each thread uses the same likelihood by default.
    For per-thread likelihood, use 'name:likelihood' syntax (e.g. 'Letter arrived:likely').
    """
    results = []
    for raw in threads:
        if ":" in raw:
            thread_name, thread_likelihood = raw.rsplit(":", 1)
            thread_name = thread_name.strip()
            thread_likelihood = thread_likelihood.strip()
        else:
            thread_name = raw
            thread_likelihood = likelihood

        roll = roll_oracle(thread_likelihood)
        roll["thread"] = thread_name
        results.append(roll)

    summary_lines = []
    for r in results:
        mod_marker = ""
        if r["modifier"] == "boon":
            mod_marker = " ⊕"
        elif r["modifier"] == "bane":
            mod_marker = " ⊖"
        summary_lines.append(
            f"| {r['thread']} | {r['likelihood']} | {r['die1']}/{r['die2']}/{r['die3']}{mod_marker} | **{r['result']}** |"
        )

    return {
        "type": "oracle_batch",
        "count": len(threads),
        "results": results,
        "table": (
            "| Thread | Likelihood | D1/D2/D3 | Result |\n"
            "|--------|------------|----------|--------|\n"
            + "\n".join(summary_lines)
        ),
    }


def parse_dice_expression(expression: str) -> dict:
    r"""
    Parse a dice expression like "2d20kh1+5" into its components.

    The pattern breaks down as:
    - (\d+)d(\d+)  : "2d20" -> count=2, sides=20
    - (k[hl]\d+)?  : "kh1" -> keep highest 1 (optional)
    - ([+-]\d+)?   : "+5" -> modifier (optional)
    """
    pattern = r'^(\d+)d(\d+)(k[hl]\d+)?([+-]\d+)?$'
    match = re.match(pattern, expression.lower().replace(' ', ''))

    if not match:
        raise ValueError(f"Invalid dice expression: {expression}")

    count = int(match.group(1))
    sides = int(match.group(2))
    keep_str = match.group(3)
    mod_str = match.group(4)

    keep_mode = None
    keep_count = None
    if keep_str:
        keep_mode = 'highest' if keep_str[1] == 'h' else 'lowest'
        keep_count = int(keep_str[2:])

    modifier = int(mod_str) if mod_str else 0

    return {
        "count": count,
        "sides": sides,
        "keep_mode": keep_mode,
        "keep_count": keep_count,
        "modifier": modifier,
    }


def roll_dice(expression: str) -> dict:
    """
    Roll dice according to the expression and return detailed results.

    Examples:
    - "1d20+5" -> roll one d20, add 5
    - "2d20kh1+3" -> roll two d20s, keep the highest, add 3 (advantage)
    - "2d20kl1" -> roll two d20s, keep the lowest (disadvantage)
    """
    parsed = parse_dice_expression(expression)

    rolls = [random.randint(1, parsed["sides"]) for _ in range(parsed["count"])]

    if parsed["keep_mode"] == 'highest':
        sorted_rolls = sorted(rolls, reverse=True)
        kept = sorted_rolls[:parsed["keep_count"]]
        dropped = sorted_rolls[parsed["keep_count"]:]
    elif parsed["keep_mode"] == 'lowest':
        sorted_rolls = sorted(rolls)
        kept = sorted_rolls[:parsed["keep_count"]]
        dropped = sorted_rolls[parsed["keep_count"]:]
    else:
        kept = rolls
        dropped = []

    dice_total = sum(kept)
    final_total = dice_total + parsed["modifier"]

    result = {
        "type": "dice",
        "expression": expression,
        "rolls": rolls,
        "kept": kept,
        "dropped": dropped,
        "dice_total": dice_total,
        "modifier": parsed["modifier"],
        "total": final_total,
    }

    if dropped:
        kept_str = '+'.join(str(k) for k in kept)
        dropped_str = ', '.join(str(d) for d in dropped)
        result["breakdown"] = f"Rolled {rolls} → kept {kept} ({kept_str}), dropped [{dropped_str}]"
    else:
        result["breakdown"] = f"Rolled {rolls}"

    if parsed["modifier"] != 0:
        sign = '+' if parsed["modifier"] > 0 else ''
        result["breakdown"] += f" {sign}{parsed['modifier']} = {final_total}"
    else:
        result["breakdown"] += f" = {final_total}"

    return result


def main():
    if len(sys.argv) < 2:
        print("Usage: python dice.py <expression>")
        print("Examples:")
        print('  python dice.py "1d20+5"')
        print('  python dice.py "2d20kh1+3"')
        print('  python dice.py oracle')
        print('  python dice.py oracle very_likely')
        print('  python dice.py oracle-batch "Thread 1" "Thread 2" "Thread 3"')
        print('  python dice.py oracle-batch --likelihood likely "Thread A" "Thread B"')
        sys.exit(1)

    expression = sys.argv[1].strip()

    try:
        if expression.lower() == "oracle":
            likelihood = sys.argv[2] if len(sys.argv) >= 3 else "fifty_fifty"
            result = roll_oracle(likelihood)
        elif expression.lower() == "oracle-batch":
            args = sys.argv[2:]
            batch_likelihood = "fifty_fifty"
            if args and args[0] == "--likelihood":
                if len(args) < 2:
                    print("Error: --likelihood requires a value")
                    sys.exit(1)
                batch_likelihood = args[1]
                args = args[2:]
            if not args:
                print("Error: oracle-batch requires at least one thread name")
                print('Usage: python dice.py oracle-batch [--likelihood L] "Thread 1" "Thread 2" ...')
                sys.exit(1)
            result = roll_oracle_batch(args, batch_likelihood)
        else:
            result = roll_dice(expression)

        print(json.dumps(result, indent=2))

    except ValueError as e:
        error_result = {"error": str(e)}
        print(json.dumps(error_result, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
