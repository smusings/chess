class Tile(object):
    is_black = False
    piece = None

    def __init__(self, is_black=False, piece=None):
        self.is_black = is_black
        self.piece = piece
