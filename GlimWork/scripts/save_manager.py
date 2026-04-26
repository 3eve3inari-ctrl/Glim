#!/usr/bin/env python3
"""
save_manager.py - Manage campaign save snapshots

Usage:
    python save_manager.py snapshot --chapter 16 --path /campaign/folder
    python save_manager.py list --path /campaign/folder
    python save_manager.py restore --chapter 12 --path /campaign/folder

Actions:
    snapshot: Copy current.md → saves/chapter-XX.md
    list: Show all available save snapshots
    restore: Copy a saved chapter back to current.md
"""

import sys
import os
import re
import shutil
import argparse
from pathlib import Path
from datetime import datetime


def get_saves_dir(campaign_path: Path) -> Path:
    """Get the saves directory, creating it if needed."""
    saves_dir = campaign_path / "saves"
    saves_dir.mkdir(exist_ok=True)
    return saves_dir


def snapshot(campaign_path: str, chapter: int) -> str:
    """
    Create a snapshot of the current game state.
    
    This copies current.md to saves/chapter-XX.md and updates
    the chapter number in current.md's header.
    """
    campaign = Path(campaign_path).resolve()
    current_file = campaign / "current.md"
    
    # Validate current.md exists
    if not current_file.exists():
        raise FileNotFoundError(f"No current.md found in {campaign}")
    
    # Create the saves directory
    saves_dir = get_saves_dir(campaign)
    
    # Format chapter number with leading zeros (e.g., chapter-03.md)
    chapter_filename = f"chapter-{chapter:02d}.md"
    save_path = saves_dir / chapter_filename
    
    # Copy current.md to the save location
    shutil.copy2(current_file, save_path)
    
    # Now update current.md to reflect the new chapter
    # We look for a line like "## Chapter X" or "## Session X" and increment it
    content = current_file.read_text()
    
    # Try to update the chapter/session header
    # This pattern matches "## Chapter 5" or "## Session 12" etc.
    chapter_pattern = r'(##\s*(?:Chapter|Session)\s*)(\d+)'
    
    def increment_chapter(match):
        prefix = match.group(1)
        new_num = chapter + 1
        return f"{prefix}{new_num}"
    
    updated_content = re.sub(chapter_pattern, increment_chapter, content, count=1)
    
    # If we made a change, write it back
    if updated_content != content:
        current_file.write_text(updated_content)
        print(f"  Updated current.md header to Chapter/Session {chapter + 1}")
    
    return str(save_path)


def list_saves(campaign_path: str) -> list:
    """
    List all available save snapshots for a campaign.
    
    Returns a list of (chapter_number, filename, modified_date) tuples.
    """
    campaign = Path(campaign_path).resolve()
    saves_dir = campaign / "saves"
    
    if not saves_dir.exists():
        return []
    
    saves = []
    
    # Find all chapter-XX.md files
    for save_file in sorted(saves_dir.glob("chapter-*.md")):
        # Extract chapter number from filename
        match = re.search(r'chapter-(\d+)\.md', save_file.name)
        if match:
            chapter_num = int(match.group(1))
            modified = datetime.fromtimestamp(save_file.stat().st_mtime)
            saves.append({
                "chapter": chapter_num,
                "filename": save_file.name,
                "path": str(save_file),
                "modified": modified.strftime("%Y-%m-%d %H:%M"),
            })
    
    return saves


def restore(campaign_path: str, chapter: int) -> str:
    """
    Restore a saved chapter as the current game state.
    
    This copies saves/chapter-XX.md back to current.md.
    Warning: This overwrites your current progress!
    """
    campaign = Path(campaign_path).resolve()
    saves_dir = get_saves_dir(campaign)
    
    # Find the save file
    chapter_filename = f"chapter-{chapter:02d}.md"
    save_path = saves_dir / chapter_filename
    
    if not save_path.exists():
        raise FileNotFoundError(f"No save found: {save_path}")
    
    current_file = campaign / "current.md"
    
    # Before overwriting, create a backup
    if current_file.exists():
        backup_path = campaign / "current.md.backup"
        shutil.copy2(current_file, backup_path)
        print(f"  Backed up current state to: current.md.backup")
    
    # Restore the save
    shutil.copy2(save_path, current_file)
    
    return str(current_file)


def main():
    parser = argparse.ArgumentParser(
        description="Manage campaign save snapshots"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Snapshot command
    snap_parser = subparsers.add_parser("snapshot", help="Save current progress")
    snap_parser.add_argument("--chapter", "-c", type=int, required=True,
                             help="Chapter number for this save")
    snap_parser.add_argument("--path", "-p", required=True,
                             help="Path to campaign folder")
    
    # List command
    list_parser = subparsers.add_parser("list", help="List available saves")
    list_parser.add_argument("--path", "-p", required=True,
                             help="Path to campaign folder")
    
    # Restore command
    restore_parser = subparsers.add_parser("restore", help="Restore a saved chapter")
    restore_parser.add_argument("--chapter", "-c", type=int, required=True,
                                help="Chapter number to restore")
    restore_parser.add_argument("--path", "-p", required=True,
                                help="Path to campaign folder")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    try:
        if args.command == "snapshot":
            print(f"Creating snapshot for chapter {args.chapter}...")
            result = snapshot(args.path, args.chapter)
            print(f"✓ Saved: {result}")
            
        elif args.command == "list":
            saves = list_saves(args.path)
            if not saves:
                print("No saves found.")
            else:
                print("Available saves:")
                print("-" * 50)
                for save in saves:
                    print(f"  Chapter {save['chapter']:2d}  |  {save['modified']}  |  {save['filename']}")
                print("-" * 50)
                print(f"Total: {len(saves)} save(s)")
                
        elif args.command == "restore":
            print(f"Restoring chapter {args.chapter}...")
            result = restore(args.path, args.chapter)
            print(f"✓ Restored to: {result}")
            
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

