def print_board(board):
    for row in board:
        print(' '.join(row))

def is_safe(board, row, col):
    # Check the column above
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 'Q':
            return False

    return True

def solve_queens(board, row):
    if row == len(board):
        # All Queens have been successfully placed
        print_board(board)
        print("\n")
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            solve_queens(board, row + 1)
            board[row][col] = '.'  # Backtrack

# Create an empty 8x8 chessboard
board = [['.' for _ in range(8)] for _ in range(8)]

# Place the first Queen at (0, 0)
board[0][0] = 'Q'

# Start the backtracking algorithm
solve_queens(board, 1)

