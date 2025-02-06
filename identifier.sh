#!/bin/bash

# Define the target directory
directory="local-cd/cdda:host=sr0"

# Check if the target is not a directory
if [ ! -d "$directory" ]; then
  echo "not dir"
  exit 1
fi

# reset tracklist
rm currentTracklist.txt
# Loop through files in the target directory
for file in "$directory"/*; do
  if [ -f "$file" ]; then
    python3 aidmatch.py "$file" >> currentTracklist.txt
  fi
done
