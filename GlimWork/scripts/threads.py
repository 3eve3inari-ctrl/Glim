#!/usr/bin/env python3
"""
threads.py - Active thread tracker for campaign saves

Parses the "Active Threads" section from a save file and helps manage them.

Usage:
    python threads.py current.md list              # List all threads
    python threads.py current.md resolve 3         # Mark thread #3 resolved
    python threads.py current.md spawn "Name" "Description"  # Add new thread
    python threads.py current.md check             # Review prompts for stale threads

Output: JSON with thread information or updated markdown
"""

import sys
import json
import re
from pathlib import Path
from datetime import datetime


def normalize_dashes(text: str) -> str:
    """
    Normalize various dash representations to a standard em-dash.
    Handles mojibake from double-encoding issues.
    """
    # Common mojibake: â€" (â + € + ") - em-dash encoded as UTF-8, read as Windows-1252, re-encoded
    # Using explicit unicode: U+00E2 + U+20AC + U+201D
    mojibake = '\u00e2\u20ac\u201d'
    text = text.replace(mojibake, '—')
    # Standard em-dash variations
    text = text.replace('–', '—')  # en-dash (U+2013)
    text = text.replace('--', '—')  # double hyphen
    return text


def extract_threads_section(content: str) -> tuple[str, int, int]:
    """
    Find the Active Threads section in a save file.
    Returns (section_text, start_index, end_index).
    """
    # Look for ## Active Threads or # Active Threads
    pattern = r'^(#{1,2}\s*Active Threads.*?)(?=^#{1,2}\s|\Z)'
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
    
    if not match:
        raise ValueError("No 'Active Threads' section found in file")
    
    return match.group(1), match.start(), match.end()


def parse_threads(section: str) -> dict:
    """
    Parse threads from the Active Threads section.
    
    Returns dict with categories as keys, each containing list of threads.
    Each thread is {number, name, description, raw_line}.
    """
    section = normalize_dashes(section)
    lines = section.split('\n')
    
    threads = {
        "_all": [],  # Flat list with all threads
        "_categories": [],  # Category names in order
    }
    
    current_category = "Uncategorized"
    thread_number = 0
    
    for line in lines:
        # Skip the main header
        if re.match(r'^#{1,2}\s*Active Threads', line):
            continue
        
        # Check for category header (### Category)
        cat_match = re.match(r'^###\s*(.+)', line)
        if cat_match:
            current_category = cat_match.group(1).strip()
            if current_category not in threads:
                threads[current_category] = []
                threads["_categories"].append(current_category)
            continue
        
        # Check for numbered thread line
        # Formats: "1. **Name** — description" or "1. **Name** - description" or just "1. Name — desc"
        # Try bold format first: "1. **Name** — description"
        thread_match = re.match(r'^(\d+)\.\s*\*\*(.+?)\*\*\s*[—\-]\s*(.+)', line)
        if not thread_match:
            # Try non-bold format: "1. Name — description"
            thread_match = re.match(r'^(\d+)\.\s*([^—\-]+?)\s*[—\-]\s*(.+)', line)
        if thread_match:
            thread_number = int(thread_match.group(1))
            name = thread_match.group(2).strip()
            description = thread_match.group(3).strip()
            
            thread_data = {
                "number": thread_number,
                "name": name,
                "description": description,
                "category": current_category,
                "raw_line": line,
            }
            
            if current_category not in threads:
                threads[current_category] = []
                threads["_categories"].append(current_category)
            
            threads[current_category].append(thread_data)
            threads["_all"].append(thread_data)
            continue
        
        # Also catch simpler format: "- **Name** — description" (unnumbered)
        unnumbered_match = re.match(r'^[-*]\s*\*\*(.+?)\*\*\s*[—\-]\s*(.+)', line)
        if not unnumbered_match:
            unnumbered_match = re.match(r'^[-*]\s*([^—\-]+?)\s*[—\-]\s*(.+)', line)
        if unnumbered_match:
            thread_number += 1
            name = unnumbered_match.group(1).strip()
            description = unnumbered_match.group(2).strip()
            
            thread_data = {
                "number": thread_number,
                "name": name,
                "description": description,
                "category": current_category,
                "raw_line": line,
            }
            
            if current_category not in threads:
                threads[current_category] = []
                threads["_categories"].append(current_category)
            
            threads[current_category].append(thread_data)
            threads["_all"].append(thread_data)
    
    return threads


def list_threads(threads: dict) -> dict:
    """Format threads for display."""
    output = {
        "type": "thread_list",
        "total": len(threads["_all"]),
        "categories": {},
        "summary": [],
    }
    
    for cat in threads["_categories"]:
        output["categories"][cat] = []
        for t in threads[cat]:
            output["categories"][cat].append({
                "number": t["number"],
                "name": t["name"],
                "description": t["description"][:60] + "..." if len(t["description"]) > 60 else t["description"],
            })
            output["summary"].append(f"{t['number']}. [{cat}] {t['name']}")
    
    return output


def resolve_thread(content: str, thread_num: int, threads: dict) -> tuple[str, dict]:
    """
    Mark a thread as resolved by moving it to a Resolved Threads section
    or commenting it out.
    
    Returns (updated_content, resolved_thread_info).
    """
    content = normalize_dashes(content)
    
    # Find the thread
    target = None
    for t in threads["_all"]:
        if t["number"] == thread_num:
            target = t
            break
    
    if not target:
        raise ValueError(f"Thread #{thread_num} not found")
    
    # Remove the line from content
    updated = content.replace(target["raw_line"] + "\n", "")
    
    # Check if there's a Resolved Threads section
    resolved_section = re.search(r'^#{1,2}\s*Resolved Threads', updated, re.MULTILINE)
    
    timestamp = datetime.now().strftime("%Y-%m-%d")
    resolved_entry = f"- ~~{target['name']}~~ — Resolved {timestamp}"
    
    if resolved_section:
        # Add to existing section
        insert_pos = resolved_section.end()
        # Find end of header line
        newline_pos = updated.find('\n', insert_pos)
        if newline_pos != -1:
            updated = updated[:newline_pos+1] + resolved_entry + "\n" + updated[newline_pos+1:]
    else:
        # Create new section after Active Threads
        section_text, start, end = extract_threads_section(updated)
        resolved_section_text = f"\n\n## Resolved Threads\n{resolved_entry}\n"
        updated = updated[:end] + resolved_section_text + updated[end:]
    
    return updated, {
        "type": "thread_resolved",
        "thread": target,
        "message": f"Resolved: {target['name']}",
    }


def spawn_thread(content: str, name: str, description: str, 
                  category: str = "Immediate") -> tuple[str, dict]:
    """
    Add a new thread to the Active Threads section.
    
    Returns (updated_content, new_thread_info).
    """
    content = normalize_dashes(content)
    section_text, start, end = extract_threads_section(content)
    threads = parse_threads(section_text)
    
    # Find the highest thread number
    max_num = max((t["number"] for t in threads["_all"]), default=0)
    new_num = max_num + 1
    
    new_line = f"{new_num}. **{name}** — {description}"
    
    # Find where to insert based on category
    if category in threads and threads[category]:
        # Insert after last thread in this category
        last_thread = threads[category][-1]
        insert_after = last_thread["raw_line"]
        insert_pos = content.find(insert_after) + len(insert_after)
        # Find the newline
        newline_pos = content.find('\n', insert_pos)
        if newline_pos != -1:
            content = content[:newline_pos+1] + new_line + "\n" + content[newline_pos+1:]
        else:
            content = content + "\n" + new_line
    else:
        # Add category if it doesn't exist, or add to end of section
        # For simplicity, add to end of Active Threads section
        content = content[:end].rstrip() + "\n" + new_line + "\n" + content[end:]
    
    return content, {
        "type": "thread_spawned",
        "number": new_num,
        "name": name,
        "description": description,
        "category": category,
    }


def check_threads(threads: dict) -> dict:
    """
    Generate review prompts for thread maintenance.
    """
    prompts = []
    
    total = len(threads["_all"])
    
    if total > 15:
        prompts.append({
            "type": "warning",
            "message": f"You have {total} active threads. Consider resolving some or consolidating related threads.",
        })
    
    if total > 0:
        prompts.append({
            "type": "review",
            "message": "Review each thread - should any be resolved, split, or merged?",
            "threads": [f"{t['number']}. {t['name']}" for t in threads["_all"]],
        })
    
    # Check for threads that might be stale based on keywords
    stale_keywords = ["pending", "waiting", "tbd", "unknown", "unclear"]
    potentially_stale = []
    for t in threads["_all"]:
        desc_lower = t["description"].lower()
        if any(kw in desc_lower for kw in stale_keywords):
            potentially_stale.append(t)
    
    if potentially_stale:
        prompts.append({
            "type": "attention",
            "message": "These threads may need updates:",
            "threads": [f"{t['number']}. {t['name']}: {t['description'][:40]}..." for t in potentially_stale],
        })
    
    return {
        "type": "thread_check",
        "total": total,
        "prompts": prompts,
    }


def main():
    if len(sys.argv) < 3:
        print("Usage: python threads.py <save_file> <command> [args]")
        print()
        print("Commands:")
        print("  list                    Show all active threads")
        print("  resolve <number>        Mark thread as resolved")
        print("  spawn <name> <desc>     Add new thread")
        print("  check                   Review prompts for thread maintenance")
        print()
        print("Examples:")
        print('  python threads.py current.md list')
        print('  python threads.py current.md resolve 5')
        print('  python threads.py current.md spawn "New threat" "Description here"')
        sys.exit(1)
    
    save_file = sys.argv[1]
    command = sys.argv[2].lower()
    
    try:
        path = Path(save_file)
        if not path.exists():
            raise FileNotFoundError(f"Save file not found: {save_file}")
        
        content = path.read_text()
        content = normalize_dashes(content)
        section_text, _, _ = extract_threads_section(content)
        threads = parse_threads(section_text)
        
        if command == "list":
            result = list_threads(threads)
            print(json.dumps(result, indent=2))
        
        elif command == "resolve":
            if len(sys.argv) < 4:
                print("Error: resolve requires a thread number")
                sys.exit(1)
            thread_num = int(sys.argv[3])
            updated_content, result = resolve_thread(content, thread_num, threads)
            path.write_text(updated_content)
            print(json.dumps(result, indent=2))
        
        elif command == "spawn":
            if len(sys.argv) < 5:
                print("Error: spawn requires name and description")
                print('Usage: python threads.py file.md spawn "Name" "Description"')
                sys.exit(1)
            name = sys.argv[3]
            description = sys.argv[4]
            category = sys.argv[5] if len(sys.argv) > 5 else "Immediate"
            updated_content, result = spawn_thread(content, name, description, category)
            path.write_text(updated_content)
            print(json.dumps(result, indent=2))
        
        elif command == "check":
            result = check_threads(threads)
            print(json.dumps(result, indent=2))
        
        else:
            print(f"Unknown command: {command}")
            sys.exit(1)
    
    except (FileNotFoundError, ValueError) as e:
        print(json.dumps({"error": str(e)}, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()