#!/bin/bash
# Package GlimGame skill into a zip file

SCRIPT_DIR="$(dirname "$0")"
cd "$SCRIPT_DIR/GlimWork" || exit 1

ZIP_NAME="../GlimGame.zip"

# Remove old zip if it exists
rm -f "$ZIP_NAME"

# Create zip with GlimWork contents at root level
zip -r "$ZIP_NAME" . \
    -x ".git/*" \
    -x "__pycache__/*" \
    -x "*.pyc"

echo "Created GlimGame.zip"
