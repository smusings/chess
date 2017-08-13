class piece(object):
    isBlack = None
    has_moved = False

    def __init__(self, isBlack=False):
        self.isBlack = isBlack

    def mark_as_moved(self):
        self.has_moved = True