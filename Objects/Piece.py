class Piece(object):
    isBlack = None

    def __init__(self, isBlack=False):
        self.isBlack = isBlack

    def move(self):
        return True