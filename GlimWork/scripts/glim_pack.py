#!/usr/bin/env python3
"""
glim_pack.py - Pack a campaign folder into a .glim bundle

Usage:
    python glim_pack.py /path/to/campaign-folder

Output:
    Creates campaign-folder.glim in the same parent directory

A .glim file is just a zip archive with a different extension.
This makes campaigns portable and easy to share.
"""

import sys
import os
import zipfile
from pathlib import Path


def pack_campaign(folder_path: str) -> str:
    """
    Pack a campaign folder into a .glim file.
    
    Args:
        folder_path: Path to the campaign folder
        
    Returns:
        Path to the created .glim file
    """
    folder = Path(folder_path).resolve()
    
    # Validate the folder exists
    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder}")
    
    if not folder.is_dir():
        raise ValueError(f"Not a directory: {folder}")
    
    # The .glim file goes in the same parent directory as the campaign folder
    # e.g., /campaigns/my-campaign/ → /campaigns/my-campaign.glim
    glim_path = folder.parent / f"{folder.name}.glim"
    
    # Create the zip file
    # We use ZIP_DEFLATED for compression
    with zipfile.ZipFile(glim_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Walk through all files in the folder
        for file_path in folder.rglob('*'):
            if file_path.is_file():
                # Calculate the path relative to the campaign folder
                # This preserves the folder structure inside the zip
                relative_path = file_path.relative_to(folder)
                
                # Add the file to the zip
                zf.write(file_path, relative_path)
                print(f"  Added: {relative_path}")
    
    return str(glim_path)


def main():
    if len(sys.argv) != 2:
        print("Usage: python glim_pack.py /path/to/campaign-folder")
        print()
        print("Packs a campaign folder into a portable .glim bundle.")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    
    try:
        print(f"Packing campaign: {folder_path}")
        result_path = pack_campaign(folder_path)
        print()
        print(f"✓ Created: {result_path}")
        
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

