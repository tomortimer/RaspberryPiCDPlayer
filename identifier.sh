#!/bin/bash

# Define the target directory
directory="."

# Check if the target is not a directory
if [ ! -d "$directory" ]; then
  echo "not dir"
  exit 1
fi

# Loop through files in the target directory
for file in "$directory"/*; do
  if [ -f "$file" ]; then
    echo "$file"
  fi
done