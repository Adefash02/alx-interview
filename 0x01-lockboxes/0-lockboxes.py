#!/usr/bin/python3

from typing import List

def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Check if all boxes can be opened.

    Parameters:
    boxes: List of lists containing keys for other boxes.

    Returns:
    True if all boxes can be opened, False otherwise.
    """
    
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys_to_check = boxes[0]
    visited = set()
    
    while keys_to_check:
        key = keys_to_check.pop()
        if key < n and key not in visited:
            visited.add(key)
            unlocked[key] = True
            keys_to_check.extend(boxes[key])
    
    return all(unlocked)

