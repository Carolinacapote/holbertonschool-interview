#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens
on an NxN chessboard.
"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

N = sys.argv[1]

if not str.isdigit(N):
    print("N must be a number")
    exit(1)

N = int(N)

if N < 4:
    print("N must be at least 4")
    exit(1)

positions = [-1] * N


def set_queen_position(N, col, positions):
    """
    Set the position of the queen in the array
    """
    for row in range(N):
        if row in positions:
            continue
        if check_diagonals(row, col, positions):
            continue
        positions[col] = row
        if col == N-1:
            print_posible_positions(N, positions)
            positions[col] = -1
            continue
        set_queen_position(N, col+1, positions)
        if -1 in positions:
            positions[col] = -1


def print_posible_positions(N, positions):
    """print the positions of the queens"""
    arr = []
    for i in range(N):
        arr.append([i, positions[i]])
    print(arr)


def check_diagonals(row, col, positions):
    """check if the queen is in the diagonal"""
    for col in range(col, -1, -1):
        if abs(positions[col] - row) == abs(col - col):
            return True
    return False


for row in range(N):
    positions[0] = row
    set_queen_position(N, 1, positions)
    positions = [-1] * N
