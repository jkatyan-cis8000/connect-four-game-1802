from typing import Tuple


class Board:
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.grid = [['.' for _ in range(self.cols)] for _ in range(self.rows)]

    def is_valid_move(self, column: int) -> bool:
        if column < 1 or column > 7:
            return False
        col_idx = column - 1
        # Check if top row is empty (column not full)
        return self.grid[self.rows - 1][col_idx] == '.'

    def apply_move(self, column: int, player: str) -> Tuple[int, int]:
        col_idx = column - 1
        for row in range(self.rows):
            if self.grid[row][col_idx] == '.':
                self.grid[row][col_idx] = player
                return (row, col_idx)
        return (-1, -1)

    def check_winner(self, row: int, col: int, player: str) -> bool:
        directions = [
            (0, 1),
            (1, 0),
            (1, 1),
            (1, -1)
        ]
        for dr, dc in directions:
            count = 1
            count += self._count_in_direction(row, col, dr, dc, player)
            count += self._count_in_direction(row, col, -dr, -dc, player)
            if count >= 4:
                return True
        return False

    def _count_in_direction(self, row: int, col: int, dr: int, dc: int, player: str) -> int:
        count = 0
        r, c = row + dr, col + dc
        while 0 <= r < self.rows and 0 <= c < self.cols and self.grid[r][c] == player:
            count += 1
            r += dr
            c += dc
        return count

    def is_full(self) -> bool:
        for col in range(self.cols):
            # Check if top row is empty (column not full)
            if self.grid[self.rows - 1][col] == '.':
                return False
        return True

    def __str__(self) -> str:
        lines = []
        for row in range(self.rows - 1, -1, -1):
            lines.append('|' + '|'.join(self.grid[row]) + '|')
        lines.append('+-------+')
        lines.append(' 1234567 ')
        return '\n'.join(lines)
