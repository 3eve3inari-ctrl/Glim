#!/usr/bin/env python3
"""
log_search.py — Search session logs for matching entries.

Returns complete session entries (not individual lines) so context is preserved.
Each entry = one "### Chapter X, Session Y" block.

Usage:
    python log_search.py <session_log_path> <pattern> [--case-sensitive]

Examples:
    python log_search.py session-log.md "Isolde"
    python log_search.py session-log.md "dragon|wyrm" 
    python log_search.py session-log.md "Chapter 15"
"""

import re
import sys
import argparse
from pathlib import Path


def parse_session_entries(content: str) -> list[dict]:
    """
    Split a session log into individual entries.
    
    Returns a list of dicts:
        {
            'header': 'Chapter 15, Session 2',
            'body': 'Full text of the entry...',
            'raw': 'Complete block including header'
        }
    """
    entries = []
    
    # Pattern matches "### Chapter X, Session Y" headers
    # Captures everything until the next ### or end of file
    pattern = r'###\s+(Chapter\s+\d+,\s+Session\s+\d+)\s*\n(.*?)(?=\n###|\Z)'
    
    matches = re.finditer(pattern, content, re.DOTALL | re.IGNORECASE)
    
    for match in matches:
        header = match.group(1).strip()
        body = match.group(2).strip()
        raw = match.group(0).strip()
        
        entries.append({
            'header': header,
            'body': body,
            'raw': raw
        })
    
    return entries


def search_entries(entries: list[dict], pattern: str, case_sensitive: bool = False) -> list[dict]:
    """
    Search entries for a regex pattern.
    Returns entries where the pattern matches anywhere in the entry (header or body).
    """
    flags = 0 if case_sensitive else re.IGNORECASE
    
    try:
        regex = re.compile(pattern, flags)
    except re.error as e:
        print(f"Invalid regex pattern: {e}", file=sys.stderr)
        sys.exit(1)
    
    matches = []
    for entry in entries:
        # Search in both header and body
        if regex.search(entry['header']) or regex.search(entry['body']):
            matches.append(entry)
    
    return matches


def format_results(matches: list[dict], pattern: str) -> str:
    """Format search results for display."""
    if not matches:
        return f"No entries found matching: {pattern}"
    
    output_lines = [
        f"Found {len(matches)} matching entry/entries for: {pattern}",
        "=" * 50
    ]
    
    for entry in matches:
        output_lines.append(f"\n### {entry['header']}")
        output_lines.append(entry['body'])
        output_lines.append("-" * 30)
    
    return "\n".join(output_lines)


def main():
    parser = argparse.ArgumentParser(
        description="Search session log for matching entries.",
        epilog="Returns complete session blocks, not individual lines."
    )
    parser.add_argument("log_path", help="Path to session-log.md")
    parser.add_argument("pattern", help="Regex pattern to search for")
    parser.add_argument(
        "--case-sensitive", "-c",
        action="store_true",
        help="Make search case-sensitive (default: case-insensitive)"
    )
    parser.add_argument(
        "--headers-only", "-H",
        action="store_true", 
        help="Only show matching headers, not full entries"
    )
    
    args = parser.parse_args()
    
    # Read the session log
    log_path = Path(args.log_path)
    if not log_path.exists():
        print(f"File not found: {log_path}", file=sys.stderr)
        sys.exit(1)
    
    content = log_path.read_text(encoding='utf-8')
    
    # Parse and search
    entries = parse_session_entries(content)
    matches = search_entries(entries, args.pattern, args.case_sensitive)
    
    # Output
    if args.headers_only:
        if not matches:
            print(f"No entries found matching: {args.pattern}")
        else:
            print(f"Found {len(matches)} matching entry/entries:")
            for entry in matches:
                print(f"  - {entry['header']}")
    else:
        print(format_results(matches, args.pattern))


if __name__ == "__main__":
    main()

