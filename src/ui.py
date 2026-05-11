from .board import Board


def display_board(board: Board) -> None:
    print(str(board))


def get_player_input(player: str) -> int:
    while True:
        try:
            user_input = input(f"{player}, enter column (1-7): ")
            column = int(user_input)
            if 1 <= column <= 7:
                return column
            else:
                print("Invalid column. Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")


def display_message(message: str) -> None:
    print(message)


def main() -> None:
    board = Board()
    current_player = "Player 1"
    player_symbol = "X"
    
    while True:
        display_board(board)
        
        column = get_player_input(current_player)
        
        if not board.is_valid_move(column):
            display_message("Invalid move. Column is full.")
            continue
        
        row, col = board.apply_move(column, player_symbol)
        
        if board.check_winner(row, col, player_symbol):
            display_board(board)
            display_message(f"{current_player} wins!")
            break
        
        if board.is_full():
            display_board(board)
            display_message("It's a draw!")
            break
        
        current_player = "Player 2" if current_player == "Player 1" else "Player 1"
        player_symbol = "O" if player_symbol == "X" else "X"


if __name__ == "__main__":
    main()
