#include <iostream>
#include <vector>
using namespace std;

// Insertion Sort Algorithm
// Time Complexity: O(n^2)
// Space Complexity: O(1)
void insertionSort(vector<int>& arr) {
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        
        // Move elements greater than key one position ahead
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

void printArray(const vector<int>& arr) {
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;
}

int main() {
    vector<int> arr = {12, 11, 13, 5, 6};
    
    cout << "Original array: ";
    printArray(arr);
    
    insertionSort(arr);
    
    cout << "Sorted array: ";
    printArray(arr);
    
    return 0;
}
