class Square:

    def __init__(self):
        self._is_open = True
        self._player = " "
        self._neighbours = []

    def is_open(self):
        return self._is_open

    def play_turn(self, player):
        self._player = player
        self._is_open = False

    def is_winner(self):
        for neighbours in self._neighbours:
            if self == neighbours[0] and self == neighbours[1]:
                return True
        return False

    def add_neighbours(self, new):
        self._neighbours = new

    def get_neighbours(self):
        return self._neighbours

    def get_player(self):
        return self._player

    def __eq__(self, other):
        return self._player == other.get_player()

    def __str__(self):
        return self._player
