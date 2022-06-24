#!/usr/bin/python3
""" Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and
including n, they take turns choosing a prime number from the set and removing that number and 
its multiples from the set. The player that cannot make a move loses the game. """


def isWinner(x, nums):
    """They play x rounds of the game, where n may be different for each round.
    Assuming Maria always goes first and both players play optimally, determine who the winner of
    each game is."""
    if not nums or x < 1:
        return None
    n = max(nums)
    new_list = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not new_list[i]:
            continue
        for j in range(i*i, n + 1, i):
            new_list[j] = False

    new_list[0] = new_list[1] = False
    c = 0
    for i in range(len(new_list)):
        if new_list[i]:
            c += 1
        new_list[i] = c

    player1 = 0
    for n in nums:
        player1 += new_list[n] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
