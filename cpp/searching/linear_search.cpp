#include <iostream>
#include <vector>
using namespace std;

// Linear Search Algorithm
// Time Complexity: O(n)
// Space Complexity: O(1)
int linearSearch(const vector<int>& arr, int target) {
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1; // Element not found
}

int main() {
    vector<int> arr = {2, 3, 4, 10, 40};
    int target = 10;
    
    int result = linearSearch(arr, target);
    
    if (result != -1) {
        cout << "Element found at index: " << result << endl;
    } else {
        cout << "Element not found in array" << endl;
    }
    
    return 0;
}
