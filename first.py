import os
import json
import spotipy
import spotipy.util as util
import json.decoder as JSONDecodeError
import sys
# Get username

username = sys.argv[1]

# User ID :

try:
 token = util.prompt_for_user_token(username)
except:
 os.remove(f".cache-{username}")
 token = util.prompt_for_user_token(username)

spotifyobject = spotipy.Spotify(auth=token)