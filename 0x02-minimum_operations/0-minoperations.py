#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste.
"""


def minOperations(n):
    """
    Given a number n, write a method that calculates the fewest number of
    operations needed to result in exactly n H characters in the file.

    Args:
        n (int): number of H characters

    Returns: int: minimum number of operations
    """
    if type(n) is int and n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                return minOperations(n // i) + i
    return 0
