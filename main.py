import json

with open("tokens.json") as tokens:
    keys = json.load(tokens)


class MissedConnection:
    def __init__(self, contents, image = None):
        self.contents = contents
        self.image = image

    def __repr__(self):
        return self.contents
