"""
Linear Search Algorithm
Time Complexity: O(n)
Space Complexity: O(1)
"""

def linear_search(arr, target):
    """
    Search for a target element using linear search
    
    Args:
        arr: List of elements
        target: Element to search for
    
    Returns:
        Index of the element if found, -1 otherwise
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Element not found

if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    target = 10
    
    result = linear_search(arr, target)
    
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in array")
