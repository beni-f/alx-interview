#!/usr/bin/env python3
"""
N Queens
"""
import sys
from typing import List


def is_valid(board, row, col):
    """
        Check if it's safe to place queen at board[row][col]
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_queens(N):
    """
    Solve the N queens puzzle and print all possible solutions.
    """
    board = [-1] * N
    solutions = []

    def backtrack(row):
        if row == N:
            solution = [[i, board[i]] for i in range(N)]
            solutions.append(solution)
            return
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1
    backtrack(0)
    return solutions


def mirror_result(result):
    n = len(result)
    return [n - 1 - col for col in result]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)
    solutions = solve_queens(n)
    for solution in solutions:
        print(solution)
