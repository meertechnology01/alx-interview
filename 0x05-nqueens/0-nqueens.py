#!/usr/bin/python3
import sys

def print_usage():
    print("Usage: nqueens N")
    sys.exit(1)

def print_error(message):
    print(message)
    sys.exit(1)

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(n):
    """Solve the N queens problem and print all solutions."""
    board = [-1] * n
    solutions = []
    place_queen(board, 0, n, solutions)
    for solution in solutions:
        print(solution)

def place_queen(board, row, n, solutions):
    """Place queens using backtracking."""
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            place_queen(board, row + 1, n, solutions)
            board[row] = -1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_error("N must be a number")
    
    if N < 4:
        print_error("N must be at least 4")

    solve_nqueens(N)
