#!/bin/bash

echo "" > currentTracklist.txt
for filename in ./run/user/1000/gvfs/cdda:host=sr0/*; do
    python3 aidmatch.py ./run/user/1000/gvfs/cdda:host=sr0/$filename >> currentTracklist.txt
done
