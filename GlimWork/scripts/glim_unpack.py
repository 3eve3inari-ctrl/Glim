#!/usr/bin/env python3
"""
glim_unpack.py - Extract a .glim bundle to a working directory

Usage:
    python glim_unpack.py /path/to/campaign.glim --output /working/dir
    python glim_unpack.py /path/to/campaign.glim  # Extracts to same directory

Output:
    Extracted folder structure at the specified location

A .glim file is just a zip archive with a different extension.
"""

import sys
import os
import zipfile
import argparse
from pathlib import Path


def unpack_campaign(glim_path: str, output_dir: str = None) -> str:
    """
    Extract a .glim file to a directory.
    
    Args:
        glim_path: Path to the .glim file
        output_dir: Where to extract (defaults to same directory as .glim)
        
    Returns:
        Path to the extracted folder
    """
    glim_file = Path(glim_path).resolve()
    
    # Validate the file exists
    if not glim_file.exists():
        raise FileNotFoundError(f"File not found: {glim_file}")
    
    if not glim_file.suffix == '.glim':
        raise ValueError(f"Not a .glim file: {glim_file}")
    
    # Determine the output directory
    if output_dir:
        output = Path(output_dir).resolve()
    else:
        # Default: extract to the same directory as the .glim file
        output = glim_file.parent
    
    # The extracted folder name comes from the .glim filename
    # e.g., my-campaign.glim → my-campaign/
    folder_name = glim_file.stem  # stem removes the extension
    extract_path = output / folder_name
    
    # Create the output directory if needed
    output.mkdir(parents=True, exist_ok=True)
    
    # Extract the zip
    with zipfile.ZipFile(glim_file, 'r') as zf:
        # Extract all files to the target folder
        for member in zf.namelist():
            # Calculate the full extraction path
            target = extract_path / member
            
            print(f"  Extracting: {member}")
            
            # Extract the file
            # extractall would work too, but this gives us control over paths
            zf.extract(member, extract_path)
    
    return str(extract_path)


def main():
    parser = argparse.ArgumentParser(
        description="Extract a .glim campaign bundle"
    )
    parser.add_argument(
        "glim_file",
        help="Path to the .glim file to extract"
    )
    parser.add_argument(
        "--output", "-o",
        help="Directory to extract to (default: same as .glim location)",
        default=None
    )
    
    args = parser.parse_args()
    
    try:
        print(f"Unpacking: {args.glim_file}")
        result_path = unpack_campaign(args.glim_file, args.output)
        print()
        print(f"✓ Extracted to: {result_path}")
        
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

