"""
Binary Search Algorithm (requires sorted array)
Time Complexity: O(log n)
Space Complexity: O(1) for iterative, O(log n) for recursive
"""

def binary_search(arr, target):
    """
    Search for a target element using binary search (iterative)
    
    Args:
        arr: Sorted list of elements
        target: Element to search for
    
    Returns:
        Index of the element if found, -1 otherwise
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Element not found

def binary_search_recursive(arr, target, left=0, right=None):
    """
    Search for a target element using binary search (recursive)
    
    Args:
        arr: Sorted list of elements
        target: Element to search for
        left: Left boundary
        right: Right boundary
    
    Returns:
        Index of the element if found, -1 otherwise
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    
    if arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    target = 10
    
    result = binary_search(arr, target)
    
    if result != -1:
        print(f"Element found at index (iterative): {result}")
    else:
        print("Element not found in array")
    
    result = binary_search_recursive(arr, target)
    
    if result != -1:
        print(f"Element found at index (recursive): {result}")
    else:
        print("Element not found in array")
