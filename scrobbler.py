import pylast
import time

# API creds
f = open("api_key.txt", "r")
API_KEY = f.read()
f.close
f = open("api_secret.txt", "r")
API_SECRET = f.read()
f.close

# user creds
f = open("lastfm_uname.txt", "r")
uname = f.read()
f.close()
f = open("lastfm_pwd.txt", "r")
password_hash = pylast.md5(f.read())
f.close()

#get network obj
network = pylast.LastFMNetwork(
    api_key=API_KEY,
    api_secret=API_SECRET,
    username=uname,
    password_hash=password_hash,
)
user = network.get_user(uname)

#get cd tracklist
f = open("currentTracklist.py")
tracklist = f.read().split("\n")
f.close()

for track in tracklist():
    #grab track
    currentlyPlaying = network.get_track_by_mbid(track)
    duration = currentlyPlaying.get_duration()
    network.scrobble(currentlyPlaying.get_artist(), currentlyPlaying.get_artist(), time.time(), currentlyPlaying.get_album())
    time.sleep(duration)
