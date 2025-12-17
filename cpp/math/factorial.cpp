#include <iostream>
using namespace std;

// Factorial Algorithm
// Time Complexity: O(n)
// Space Complexity: O(1) for iterative, O(n) for recursive

// Iterative approach
long long factorialIterative(int n) {
    if (n < 0) return -1; // Error: factorial of negative number
    
    long long result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

// Recursive approach
long long factorialRecursive(int n) {
    if (n < 0) return -1; // Error: factorial of negative number
    if (n == 0 || n == 1) return 1;
    return n * factorialRecursive(n - 1);
}

int main() {
    int num = 5;
    
    cout << "Factorial of " << num << " (iterative): " 
         << factorialIterative(num) << endl;
    cout << "Factorial of " << num << " (recursive): " 
         << factorialRecursive(num) << endl;
    
    return 0;
}
