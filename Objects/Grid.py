class Grid(object):
    board = []

    def __init__(self):
        is_black = False

        for y in xrange(0,8):
            rows = []
            for x in xrange(0,8):
                rows.append({"is_black":is_black, "piece":None})
                is_black = not is_black
            self.board.append(rows)
            
    def get_possible_moves(self, piece):
        return 