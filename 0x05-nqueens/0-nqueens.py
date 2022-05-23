#!/usr/bin/python3


from curses.ascii import isdigit


def is_safe(board, row, column):
    """
    Function that check if the Queens dosn't atack each other
        board: Array of lenght n with the position of all the queens
        row: row position of the queen
        column: column position of the queen
    """

    for queen in range(column):
        if board[queen] == row or\
                abs(board[queen] - row) == abs(queen - column):
            return False

    return True


def check_board(board, column, n):
    """
    function that select and print the board:
        board: Array of lenght n with the position of all the queens
        column: column of othe position
        n = the number of queens and positions
    """
    if column == n:
        print(str([[c, board[c]] for c in range(n)]))
        return

    for row in range(n):
        if is_safe(board, row, column):
            board[column] = row
            check_board(board, column + 1, n)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")

    N = int(sys.argv[1])

    if type(N) != int:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [0 for row in range(N)]

    check_board(board, 0, N)
