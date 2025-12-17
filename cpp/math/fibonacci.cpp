#include <iostream>
#include <vector>
using namespace std;

// Fibonacci Algorithm
// Time Complexity: O(n) for iterative and DP, O(2^n) for naive recursive
// Space Complexity: O(1) for iterative, O(n) for DP and recursive

// Iterative approach
long long fibonacciIterative(int n) {
    if (n < 0) return -1;
    if (n == 0) return 0;
    if (n == 1) return 1;
    
    long long a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        long long temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

// Recursive approach (naive)
long long fibonacciRecursive(int n) {
    if (n < 0) return -1;
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

// Dynamic Programming approach
long long fibonacciDP(int n) {
    if (n < 0) return -1;
    if (n == 0) return 0;
    if (n == 1) return 1;
    
    vector<long long> dp(n + 1);
    dp[0] = 0;
    dp[1] = 1;
    
    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    
    return dp[n];
}

int main() {
    int n = 10;
    
    cout << "Fibonacci of " << n << " (iterative): " 
         << fibonacciIterative(n) << endl;
    cout << "Fibonacci of " << n << " (recursive): " 
         << fibonacciRecursive(n) << endl;
    cout << "Fibonacci of " << n << " (DP): " 
         << fibonacciDP(n) << endl;
    
    return 0;
}
