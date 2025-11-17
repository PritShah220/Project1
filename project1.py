def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Row check
            return True
        if all([board[j][i] == player for j in range(3)]):  # Column check
            return True
    if all([board[i][i] == player for i in range(3)]):  # Main diagonal
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # Anti-diagonal
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    moves = 0
    
    while moves < 9:
        print_board(board)
        try:
            row = int(input(f"Player {current_player}, enter row (1-3): ")) - 1
            col = int(input(f"Player {current_player}, enter column (1-3): ")) - 1
            if board[row][col] != " ":
                print("Cell already taken, try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input, please enter row and column as numbers between 1 and 3.")
            continue
        
        board[row][col] = current_player
        moves += 1
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return
        
        current_player = "O" if current_player == "X" else "X"
    
    print_board(board)
    print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()

