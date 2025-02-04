# RaspberryPiCDPlayer
A simple method of controlling a disk drive as if built as an integrated CD player. Not included in the repo is the config to run the controls.py at startup and focus it on an empty terminal.

aidmatch.py is from https://github.com/beetbox/pyacoustid/blob/master/aidmatch.py
It's very useful for IDing tracks, since cheap disk drives and raspbian mean a lack of metadata

## To Run Headerless:
1. Configure terminalLauncher.sh to run at startup, this ensures there is one focused terminal window in the correct directory.
2. Ensure Controls.py is running (I suggest configuring it to run at startup) and you have the buttons wired to the correct pins.
3. Press the middle button to start playback.

## Incomplete Features:
- Track ID -> Scrobbling
- Spotify API Integration (to sync played songs)
