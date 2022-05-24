#!/usr/bin/python3


def check_position(chessboard, row, col):
    """
    function that check if the position is safe
    """

    for queen in range(col):
        if chessboard[queen] == row or\
                abs(chessboard[queen] - row) == abs(queen - col):
            return False

    return True


def print_chessboard(board, col, n):
    """
    function that print the board
    """
    if col == n:
        print(str([[i, board[i]] for i in range(n)]))
        return

    for row in range(n):
        if check_position(board, row, col):
            board[col] = row
            print_chessboard(board, col + 1, n)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = [0 for row in range(N)]

    print_chessboard(chessboard, 0, N)
