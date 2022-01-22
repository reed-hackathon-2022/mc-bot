import json

keys = json.load("tokens.json")


class MissedConnection:
    def __init__(self, contents, image = None):
        self.contents = contents
        self.image = image
