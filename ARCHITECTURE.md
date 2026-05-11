# ARCHITECTURE.md

Written by team-lead before spawning teammates. This is the shared blueprint —
teammates read it to understand what they are building and how their module fits.
Update it when the structure changes; do not let it drift from the actual code.

## Module Structure

- src/board.py: 7x6 grid state, column validation, disc placement, win detection (horizontal, vertical, diagonal)
- src/game.py: turn management, player state (Player 1/Player 2), game loop, win/draw detection
- src/ui.py: terminal rendering of board, user input parsing (column number 1-7), move validation feedback

## Interfaces

### board.py
- `class Board`: 7 columns x 6 rows grid
  - `is_valid_move(column: int) -> bool`: check if column is not full and in range 1-7
  - `apply_move(column: int, player: str) -> Tuple[int, int]`: place disc, return (row, col) of placement
  - `check_winner(row: int, col: int, player: str) -> bool`: check for 4-in-a-row (horizontal, vertical, diagonal)
  - `is_full() -> bool`: check if board is full (draw condition)
  - `__str__() -> str`: render board as string for display

### game.py
- `class Game`: manages game state
  - `__init__()`: initialize board, current player (Player 1 starts)
  - `play_turn(column: int) -> Tuple[str, bool]`: execute turn, return (status message, game_over)
  - `get_current_player() -> str`: return current player ("Player 1" or "Player 2")
  - `is_game_over() -> bool`: check win or draw
  - `get_winner() -> str | None`: return winning player or None

### ui.py
- `display_board(board: Board) -> None`: render current board state
- `get_player_input(player: str) -> int`: prompt player for column (1-7), validate input
- `display_message(message: str) -> None`: show game messages (invalid move, win, draw)
- `main()`: game loop coordination

## Shared Data Structures

- `Board`: 7 columns, 6 rows, represented as list of lists or 2D array
- `Player`: "Player 1" or "Player 2" (or "X" or "O")
- `Move`: column number (1-7 integer)
- `Position`: (row, col) tuple for disc placement
- `GameState`: {"status": "playing" | "win" | "draw", "winner": str | None}

## External Dependencies

- No external dependencies required (pure Python standard library)
