class MissedConnection:
    def __init__(self, contents, image=None):
        self.contents = contents
        self.image = image

    def __repr__(self):
        return ' '.join(self.contents)