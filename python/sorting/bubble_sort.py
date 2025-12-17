"""
Bubble Sort Algorithm
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def bubble_sort(arr):
    """
    Sort an array using bubble sort algorithm
    
    Args:
        arr: List of comparable elements
    
    Returns:
        Sorted list
    """
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no elements were swapped, array is sorted
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    
    print("Original array:", arr)
    bubble_sort(arr)
    print("Sorted array:", arr)
