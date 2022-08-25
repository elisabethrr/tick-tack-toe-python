from square import Square

class Board:

    def __init__(self):
        self._board = []
        self._make_board()

    def play_turn(self, row, colonne, player):
        valid_input = self._check_input(row, colonne)
        if valid_input:
            current_placement = self._board[row][colonne]
            current_placement.play_turn(player)
            return True
        return False

    def _check_input(self, row, col):
        if row == -1 or row >= len(self._board) or col == -1 or col >= len(self._board[row-1]):
            print("Invalid input\n")
            return False

        if self._board[row][col].is_open():
            return True
        else:
            print("This square is not open\n")
            return False

    def check_winner(self, row, col):
        square = self._board[row][col]
        if square.is_winner():
            return square
        return False

    def __str__(self):
        board_interface = ""
        for row in self._board:
            board_interface += "\n-------------\n| "
            for col in row:
                board_interface += str(col)
                board_interface += " | "

        board_interface += "\n-------------\n"
        return board_interface

    def _make_board(self):
        square1 = Square()
        square12 = Square()
        square13 = Square()

        square2 = Square()
        square22 = Square()
        square23 = Square()

        square3 = Square()
        square32 = Square()
        square33 = Square()

        # Add neighbours
        square1.add_neighbours([[square12, square13], [square22, square33], [square2, square3]])
        square12.add_neighbours([[square1, square13], [square22, square32]])
        square13.add_neighbours([[square12, square1], [square22, square3], [square2, square1]])

        square2.add_neighbours([[square1, square3], [square22, square23]])
        square22.add_neighbours([[square12, square32], [square23, square2]])
        square23.add_neighbours([[square13, square33], [square22, square2]])

        square3.add_neighbours([[square1, square2], [square22, square13], [square32, square33]])
        square32.add_neighbours([[square22, square12], [square3, square33]])
        square33.add_neighbours([[square13, square23], [square22, square1], [square3, square32]])

        self._board = [
            [square1, square12, square13],
            [square2, square22, square23],
            [square3, square32, square33]
        ]