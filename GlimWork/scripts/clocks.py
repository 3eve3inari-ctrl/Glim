#!/usr/bin/env python3
"""
clocks.py - Pressure clock manager for campaign saves

Clocks live in a JSON file (default: clocks.json in the campaign folder),
parallel to other campaign memory. Each clock has a slug id, a size
(segments), filled count, scope, and an audit trail of ticks. On
completion, clocks move to a "completed" archive with a resolution note
and the full step history.

Usage:
    python clocks.py <file> create <id> <name> <size> [scope]
    python clocks.py <file> list
    python clocks.py <file> show <id>
    python clocks.py <file> tick <id> [delta] [--trigger "reason"]
    python clocks.py <file> untick <id> [delta] [--trigger "reason"]
    python clocks.py <file> complete <id> --resolution "narrative"
    python clocks.py <file> reopen <id>          # move from completed back to active

Scopes:
    tactical   (default size 4) — scene-level pressure
    encounter  (default size 6) — combat or social arc
    campaign   (default size 8) — long-term goal or faction clock

Examples:
    python clocks.py clocks.json create council-decides "Council decides on petition" 6 encounter
    python clocks.py clocks.json tick council-decides 2 --trigger "missed the morning session"
    python clocks.py clocks.json complete council-decides --resolution "Council ruled in favor; Voss owes us"
"""

import sys
import json
from pathlib import Path
from datetime import datetime


VALID_SCOPES = {"tactical", "encounter", "campaign"}
DEFAULT_SIZES = {"tactical": 4, "encounter": 6, "campaign": 8}


def load_clocks(path: Path) -> dict:
    if not path.exists():
        return {"active": {}, "completed": []}
    data = json.loads(path.read_text())
    data.setdefault("active", {})
    data.setdefault("completed", [])
    return data


def save_clocks(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2) + "\n")


def today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def render_bar(filled: int, size: int) -> str:
    filled = max(0, min(size, filled))
    return "[" + "▓" * filled + "░" * (size - filled) + "]"


def require_active(data: dict, clock_id: str) -> dict:
    if clock_id not in data["active"]:
        raise ValueError(f"No active clock with id '{clock_id}'")
    return data["active"][clock_id]


def create_clock(data: dict, clock_id: str, name: str, size: int, scope: str) -> dict:
    if clock_id in data["active"]:
        raise ValueError(f"Clock '{clock_id}' already exists")
    if scope not in VALID_SCOPES:
        raise ValueError(f"Invalid scope '{scope}'. Valid: {', '.join(sorted(VALID_SCOPES))}")
    if size < 1:
        raise ValueError("Clock size must be at least 1")
    clock = {
        "name": name,
        "size": size,
        "filled": 0,
        "scope": scope,
        "created": today(),
        "steps": [],
    }
    data["active"][clock_id] = clock
    return {
        "type": "clock_created",
        "id": clock_id,
        "clock": clock,
        "render": render_bar(0, size),
    }


def list_clocks(data: dict) -> dict:
    active_summary = []
    for cid, c in data["active"].items():
        active_summary.append({
            "id": cid,
            "name": c["name"],
            "scope": c["scope"],
            "filled": c["filled"],
            "size": c["size"],
            "render": render_bar(c["filled"], c["size"]),
        })
    completed_summary = [
        {
            "name": c["name"],
            "scope": c["scope"],
            "completed": c["completed"],
            "resolution": c.get("resolution", ""),
        }
        for c in data["completed"][-5:]
    ]
    return {
        "type": "clock_list",
        "active_count": len(active_summary),
        "active": active_summary,
        "recent_completed": completed_summary,
    }


def show_clock(data: dict, clock_id: str) -> dict:
    if clock_id in data["active"]:
        c = data["active"][clock_id]
        return {
            "type": "clock_show",
            "id": clock_id,
            "status": "active",
            "clock": c,
            "render": render_bar(c["filled"], c["size"]),
        }
    for c in data["completed"]:
        if c.get("id") == clock_id:
            return {
                "type": "clock_show",
                "id": clock_id,
                "status": "completed",
                "clock": c,
                "render": render_bar(c["size"], c["size"]),
            }
    raise ValueError(f"No clock with id '{clock_id}' (active or completed)")


def tick_clock(data: dict, clock_id: str, delta: int, trigger: str) -> dict:
    clock = require_active(data, clock_id)
    new_filled = max(0, min(clock["size"], clock["filled"] + delta))
    actual_delta = new_filled - clock["filled"]
    clock["filled"] = new_filled
    clock["steps"].append({
        "date": today(),
        "delta": actual_delta,
        "trigger": trigger,
    })
    completed = clock["filled"] >= clock["size"]
    return {
        "type": "clock_tick",
        "id": clock_id,
        "delta_requested": delta,
        "delta_applied": actual_delta,
        "filled": clock["filled"],
        "size": clock["size"],
        "render": render_bar(clock["filled"], clock["size"]),
        "completed_segments": completed,
        "hint": (
            f"Clock '{clock_id}' is full — call `complete` with a resolution narrative."
            if completed else None
        ),
    }


def complete_clock(data: dict, clock_id: str, resolution: str) -> dict:
    clock = require_active(data, clock_id)
    archived = {
        "id": clock_id,
        **clock,
        "completed": today(),
        "resolution": resolution,
    }
    data["completed"].append(archived)
    del data["active"][clock_id]
    return {
        "type": "clock_completed",
        "id": clock_id,
        "archived": archived,
    }


def reopen_clock(data: dict, clock_id: str) -> dict:
    for i, c in enumerate(data["completed"]):
        if c.get("id") == clock_id:
            restored = {k: v for k, v in c.items() if k not in ("completed", "resolution", "id")}
            data["active"][clock_id] = restored
            del data["completed"][i]
            return {
                "type": "clock_reopened",
                "id": clock_id,
                "clock": restored,
                "render": render_bar(restored["filled"], restored["size"]),
            }
    raise ValueError(f"No completed clock with id '{clock_id}'")


def parse_trigger_flag(args: list[str]) -> tuple[list[str], str]:
    """Extract --trigger / --resolution value, return (remaining, value)."""
    out = []
    value = ""
    i = 0
    while i < len(args):
        if args[i] in ("--trigger", "--resolution"):
            if i + 1 >= len(args):
                raise ValueError(f"{args[i]} requires a value")
            value = args[i + 1]
            i += 2
            continue
        out.append(args[i])
        i += 1
    return out, value


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    file_arg = sys.argv[1]
    command = sys.argv[2].lower()
    rest = sys.argv[3:]

    path = Path(file_arg)

    try:
        data = load_clocks(path)

        if command == "create":
            if len(rest) < 3:
                raise ValueError('create requires: <id> <name> <size> [scope]')
            clock_id = rest[0]
            name = rest[1]
            size = int(rest[2])
            scope = rest[3] if len(rest) >= 4 else "encounter"
            result = create_clock(data, clock_id, name, size, scope)
            save_clocks(path, data)

        elif command == "list":
            result = list_clocks(data)

        elif command == "show":
            if not rest:
                raise ValueError("show requires: <id>")
            result = show_clock(data, rest[0])

        elif command in ("tick", "untick"):
            if not rest:
                raise ValueError(f"{command} requires: <id> [delta] [--trigger \"reason\"]")
            positional, trigger = parse_trigger_flag(rest)
            clock_id = positional[0]
            delta = int(positional[1]) if len(positional) >= 2 else 1
            if command == "untick":
                delta = -delta
            if not trigger:
                trigger = "(no reason given)"
            result = tick_clock(data, clock_id, delta, trigger)
            save_clocks(path, data)

        elif command == "complete":
            if not rest:
                raise ValueError("complete requires: <id> --resolution \"narrative\"")
            positional, resolution = parse_trigger_flag(rest)
            if not resolution:
                raise ValueError("complete requires --resolution \"narrative\"")
            result = complete_clock(data, positional[0], resolution)
            save_clocks(path, data)

        elif command == "reopen":
            if not rest:
                raise ValueError("reopen requires: <id>")
            result = reopen_clock(data, rest[0])
            save_clocks(path, data)

        else:
            raise ValueError(f"Unknown command: {command}")

        print(json.dumps(result, indent=2, ensure_ascii=False))

    except (ValueError, json.JSONDecodeError, FileNotFoundError) as e:
        print(json.dumps({"error": str(e)}, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
