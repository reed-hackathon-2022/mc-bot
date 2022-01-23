import time
import json
import sys

from tweepy import API, Client, OAuthHandler


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
    if len(sys.argv) > 1:
        start = int(sys.argv[1])
    else:
        start = 0
    for connection in connections[start:]:
        if connection.image is None:
            previous_id = None
            print(connection.contents)
            for content in connection.contents:
                print(f"Tweet length: {len(content)}")
                result = client.create_tweet(
                    text=content, in_reply_to_tweet_id=previous_id
                )
                print(result)
                print(f"Successful tweet: id = {result[0]['id']}")
                previous_id = result[0]['id']
                time.sleep(30)
            time.sleep(270)
        else:
            raise NotImplementedError("Tweeting images is not implemented yet")
