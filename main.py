"""Connect Four game entry point."""

from src.game import Game


def main() -> None:
    game = Game()
    
    while True:
        print("\n" + "=" * 30)
        game.game_display()
        
        player = game.get_current_player()
        try:
            column = int(input(f"{player}, enter column (1-7): "))
            
            if column < 1 or column > 7:
                print("Invalid column. Please enter a number between 1 and 7.")
                continue
            
            message, game_over = game.play_turn(column)
            print(message)
            
            if game_over:
                print("\nFinal board:")
                game.game_display()
                if game.get_winner():
                    print(f"{game.get_winner()} wins!")
                else:
                    print("It's a draw!")
                break
                
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
