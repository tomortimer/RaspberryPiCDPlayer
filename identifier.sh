#!/bin/bash

# Define the target directory
directory="/run/user/1000/gvfs/cdda:host=sr0"

# Check if the target is not a directory
if [ ! -d "$directory" ]; then
  exit 1
fi

# Loop through files in the target directory
for file in "$directory"/*; do
  if [ -f "$file" ]; then
    echo "$file"
  fi
done