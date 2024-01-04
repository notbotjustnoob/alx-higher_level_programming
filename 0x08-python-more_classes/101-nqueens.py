#!/usr/bin/python3
import sys


def print_solution(board):
    """Print the board solution."""
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col):
    """Use backtracking to find all solutions."""
    if col >= len(board):
        print_solution(board)
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens(board, col + 1)
            board[i][col] = 0


def nqueens(n):
    """Initialize the board and start the solver."""
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_nqueens(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(n)
