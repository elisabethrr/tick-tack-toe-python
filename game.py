from board import Board

class Game:

    def __init__(self):
        self._board = Board()

    def start_game(self):
        print("\nTICK TACK TOE")
        print(self._board)
        self.play_turn()

    def play_turn(self):
        counter = 0
        while counter < 9:
            # Who's turn is it?
            player = "O"
            if counter % 2 == 0:
                player = "X"

            # Choose placement
            row = None
            col = None
            turn_finished = False
            while not turn_finished:
                print("Player ", player, " - your turn")
                row = int(input("row: "))
                row = row - 1
                col = int(input("colonne: "))
                col = col - 1
                turn_finished = self._board.play_turn(row, col, player)

            print(self._board)
            counter += 1

            # Is there a winner this round?
            winner = self._board.check_winner(row, col)
            if winner:
                print(f"Game over. THE WINNER IS {winner}!")
                exit(1)

        # No winner
        print("\nGame over. It's a tie.")


game = Game()
game.start_game()

