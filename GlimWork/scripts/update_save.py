#!/usr/bin/env python3
"""
update_save.py — Create or overwrite save files

Handles the common case where you need to update current.md or other
save files that may or may not already exist.

Usage:
    # From stdin (pipe content)
    echo "# Save content" | python scripts/update_save.py current.md
    
    # From a file
    python scripts/update_save.py current.md --from draft.md
    
    # Interactive (type content, Ctrl+D to finish)
    python scripts/update_save.py current.md

The script creates parent directories if needed and overwrites existing files.
"""

import sys
import argparse
from pathlib import Path


def update_file(target_path: str, content: str) -> str:
    """
    Write content to target file, creating directories as needed.
    Returns a status message.
    """
    path = Path(target_path).resolve()
    
    # Create parent directories if they don't exist
    path.parent.mkdir(parents=True, exist_ok=True)
    
    # Determine if this is a create or overwrite
    action = "Updated" if path.exists() else "Created"
    
    # Write the content
    path.write_text(content, encoding='utf-8')
    
    return f"{action}: {path}"


def main():
    parser = argparse.ArgumentParser(
        description="Create or overwrite save files.",
        epilog="Reads from stdin by default. Use --from to read from a file."
    )
    parser.add_argument(
        "target",
        help="Target file path to create/overwrite"
    )
    parser.add_argument(
        "--from", "-f",
        dest="source",
        help="Read content from this file instead of stdin"
    )
    
    args = parser.parse_args()
    
    # Get content from source file or stdin
    if args.source:
        source_path = Path(args.source)
        if not source_path.exists():
            print(f"Error: Source file not found: {source_path}", file=sys.stderr)
            sys.exit(1)
        content = source_path.read_text(encoding='utf-8')
    else:
        # Read from stdin
        if sys.stdin.isatty():
            print("Enter content (Ctrl+D to finish):", file=sys.stderr)
        content = sys.stdin.read()
    
    if not content.strip():
        print("Error: No content provided", file=sys.stderr)
        sys.exit(1)
    
    # Update the file
    try:
        result = update_file(args.target, content)
        print(result)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

