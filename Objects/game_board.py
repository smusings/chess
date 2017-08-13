from string import ascii_lowercase
from tile import Tile


class GameBoard(object):
    board = {}

    def __init__(self):
        is_black = False

        for letter in ascii_lowercase:
            if letter == "i":
                break
            else:
                for i in range(1,9):
                    self.board[letter+i] = Tile(is_black)
                    is_black = not is_black
            
    def get_possible_moves(self, key):
        possible_moves = []
        piece = self.board[key]

        if piece is None:
            return []

        return possible_moves