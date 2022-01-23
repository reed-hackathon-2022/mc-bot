import time
import json

from tweepy import API, OAuthHandler


with open("tokens.json") as tokens:
    keys = json.load(tokens)


def tweet_connections(connections):
    auth = OAuthHandler(keys["api"], keys["api_secret"])
    auth.set_access_token(keys["access"], keys["access_secret"])
    api = API(auth)
    for connection in connections:
        if connection.image is None:
            api.update_status(connection.contents)
            time.sleep(300)
        else:
            api.update_status_with_media(connection.contents, connection.image)
            time.sleep(300)
