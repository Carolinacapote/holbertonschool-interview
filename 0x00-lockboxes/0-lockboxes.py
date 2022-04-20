#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    Method that determines if all the boxes can be opened.
    """
    unlocked = [0]
    for box_index, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_index:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
