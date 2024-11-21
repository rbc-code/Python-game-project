def display_board(board):
    """Display the current game board."""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def is_winner(board, player):
    """Check if the given player has won."""
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_draw(board):
    """Check if the game is a draw."""
    return all(cell != " " for row in board for cell in row)


def get_player_move(player, board):
    """Prompt the current player to make a move."""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                return row, col
            else:
                print("Cell already taken, choose another.")
        except (ValueError, IndexError):
            print("Invalid move. Enter a number between 1 and 9.")


def tic_tac_toe():
    """Main function to play the Tic-Tac-Toe game."""
    print("Welcome to Tic-Tac-Toe!")
    while True:
        
        board = [[" "] * 3 for _ in range(3)]
        players = ["R", "B"]
        current_player = 0

        while True:
            display_board(board)
            row, col = get_player_move(players[current_player], board)
            board[row][col] = players[current_player]

            if is_winner(board, players[current_player]):
                display_board(board)
                print(f"Player {players[current_player]} wins!")
                break
            elif is_draw(board):
                display_board(board)
                print("It's a draw!")
                break

            current_player = 1 - current_player 

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    tic_tac_toe()
