from typing import Tuple
from .board import Board


class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = "Player 1"
        self.player_symbol = {"Player 1": "X", "Player 2": "O"}
        self.game_over = False
        self.winner = None

    def play_turn(self, column: int) -> Tuple[str, bool]:
        if self.game_over:
            return ("Game is already over", True)

        if not self.board.is_valid_move(column):
            return ("Invalid move", False)

        row, col = self.board.apply_move(column, self.player_symbol[self.current_player])

        if self.board.check_winner(row, col, self.player_symbol[self.current_player]):
            self.game_over = True
            self.winner = self.current_player
            return (f"{self.current_player} wins!", True)

        if self.board.is_full():
            self.game_over = True
            return ("Draw!", True)

        self.current_player = "Player 2" if self.current_player == "Player 1" else "Player 1"
        return ("Move successful", False)

    def get_current_player(self) -> str:
        return self.current_player

    def is_game_over(self) -> bool:
        return self.game_over

    def get_winner(self) -> str | None:
        return self.winner

    def game_display(self) -> None:
        """Display the current board state."""
        print(self.board)
