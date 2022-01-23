import json
from parser import parse
from tweeter import tweet_connections

with open("tokens.json") as tokens:
    keys = json.load(tokens)


class MissedConnection:
    def __init__(self, contents, image=None):
        self.contents = contents
        self.image = image

    def __repr__(self):
        return self.contents


def launch_bot():
    contents = parse()
    tweet_connections(contents)
