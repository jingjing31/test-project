"""
Selection Sort Algorithm
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def selection_sort(arr):
    """
    Sort an array using selection sort algorithm
    
    Args:
        arr: List of comparable elements
    
    Returns:
        Sorted list
    """
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    
    print("Original array:", arr)
    selection_sort(arr)
    print("Sorted array:", arr)
