#include <iostream>
#include <vector>
using namespace std;

// Binary Search Algorithm (requires sorted array)
// Time Complexity: O(log n)
// Space Complexity: O(1)
int binarySearch(const vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid;
        }
        
        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1; // Element not found
}

// Recursive implementation
int binarySearchRecursive(const vector<int>& arr, int target, int left, int right) {
    if (left > right) {
        return -1;
    }
    
    int mid = left + (right - left) / 2;
    
    if (arr[mid] == target) {
        return mid;
    }
    
    if (arr[mid] < target) {
        return binarySearchRecursive(arr, target, mid + 1, right);
    } else {
        return binarySearchRecursive(arr, target, left, mid - 1);
    }
}

int main() {
    vector<int> arr = {2, 3, 4, 10, 40};
    int target = 10;
    
    int result = binarySearch(arr, target);
    
    if (result != -1) {
        cout << "Element found at index (iterative): " << result << endl;
    } else {
        cout << "Element not found in array" << endl;
    }
    
    result = binarySearchRecursive(arr, target, 0, arr.size() - 1);
    
    if (result != -1) {
        cout << "Element found at index (recursive): " << result << endl;
    } else {
        cout << "Element not found in array" << endl;
    }
    
    return 0;
}
