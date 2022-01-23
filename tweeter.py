import time
import json

from tweepy import Client, OAuthHandler


with open("tokens.json") as tokens:
    keys = json.load(tokens)


def tweet_connections(connections):
    auth = OAuthHandler(keys["api"], keys["api_secret"])
    auth.set_access_token(keys["access"], keys["access_secret"])
    client = Client(
        consumer_key=keys["api"], consumer_secret=keys["api_secret"],
        access_token=keys["access"], access_token_secret=keys["access_secret"],
        bearer_token=keys["bearer_token"],
    )
    for connection in connections:
        if connection.image is None:
            client.create_tweet(text=connection.contents)
            time.sleep(300)
        else:
            raise NotImplementedError("Tweeting images is not implemented yet")
