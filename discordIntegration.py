#integrates with discord to show as a Listening activity
#relies on the scrobbler working though
from pypresence import Presence
from pypresence.types import ActivityType
import time
import pylast

#api creds
f = open("api_key.txt", "r")
API_KEY = f.read()
f.close
f = open("api_secret.txt", "r")
API_SECRET = f.read()
f.close

#user creds
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

#discord api connection
f = open("discord_api.txt", "r")
client_id = f.read() 
f.close()

RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop
current_track = None
startTime = time.time()
while True:  # The presence will stay on as long as the program is running
    img = "cd-rom"
    # try and grab track from lastfm
    try:
        track = user.get_now_playing()
    except(pylast.WSError):
        track = current_track
        print("pylast error")
        time.sleep(2)
    
    #if track has changed, update rich presence
    current_time = time.time()
    if track != None and str(current_track) != str(track):
        startTime = time.time()
        #try and grab album art
        print(track.get_cover_image())
        img = track.get_cover_image()
        current_track = track
        RPC.update(state=str(track.get_artist()), details=str(track.get_name()), activity_type=ActivityType.LISTENING, start=startTime, instance=True, large_image=img)
    elif track == None:
        RPC.clear()