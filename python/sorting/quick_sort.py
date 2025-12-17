"""
Quick Sort Algorithm
Time Complexity: O(n log n) average, O(n^2) worst case
Space Complexity: O(log n)
"""

def quick_sort(arr, low=0, high=None):
    """
    Sort an array using quick sort algorithm
    
    Args:
        arr: List of comparable elements
        low: Starting index
        high: Ending index
    
    Returns:
        Sorted list
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pi = partition(arr, low, high)
        
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    
    return arr

def partition(arr, low, high):
    """
    Partition array around a pivot
    
    Args:
        arr: List to partition
        low: Starting index
        high: Ending index
    
    Returns:
        Partition index
    """
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    
    print("Original array:", arr)
    quick_sort(arr)
    print("Sorted array:", arr)
