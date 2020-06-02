import spotipy
import spotipy.util as util
from discover.config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET

scope = 'user-top-read'


def authorize(username):
    token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, 'http://localhost'
                                                                                                  ':8000/')
    if token:
        sp = spotipy.Spotify(auth=token)
        return sp.current_user_top_artists()
    else:
        return {"username": username}
