from typing import List

def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determine if all boxes can be opened given the keys inside them.

    Parameters:
    boxes (List[List[int]]): A list of lists where each inner list contains
                              keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    
    n = len(boxes)  # Total number of boxes
    unlocked = [False] * n  # Track which boxes are unlocked
    unlocked[0] = True  # The first box is initially unlocked
    keys_to_check = boxes[0]  # Start with the keys in the first box

    # Use a set to avoid processing the same box multiple times
    visited = set()
    
    while keys_to_check:
        key = keys_to_check.pop()
        
        # Check if the key corresponds to an unopened box
        if key < n and key not in visited:
            visited.add(key)  # Mark this box as visited
            unlocked[key] = True  # Unlock the box
            # Add the keys from the newly unlocked box to the list
            keys_to_check.extend(boxes[key])
    
    # Check if all boxes are unlocked
    return all(unlocked)

# Example usage
if __name__ == "__main__":
    boxes_list = [
        [[1], [2], [3], [4], []],  # True
        [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]],  # True
        [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]  # False
    ]
    
    for boxes in boxes_list:
        result = canUnlockAll(boxes)
        print(f"Can unlock all boxes {boxes}: {result}")

