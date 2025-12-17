"""
Insertion Sort Algorithm
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def insertion_sort(arr):
    """
    Sort an array using insertion sort algorithm
    
    Args:
        arr: List of comparable elements
    
    Returns:
        Sorted list
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    
    print("Original array:", arr)
    insertion_sort(arr)
    print("Sorted array:", arr)
