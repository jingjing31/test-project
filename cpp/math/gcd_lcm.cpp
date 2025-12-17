#include <iostream>
using namespace std;

// GCD and LCM Algorithms
// Time Complexity: O(log(min(a,b)))
// Space Complexity: O(1) for iterative, O(log(min(a,b))) for recursive

// GCD using Euclidean algorithm (iterative)
int gcdIterative(int a, int b) {
    a = abs(a);
    b = abs(b);
    
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// GCD using Euclidean algorithm (recursive)
int gcdRecursive(int a, int b) {
    a = abs(a);
    b = abs(b);
    
    if (b == 0) return a;
    return gcdRecursive(b, a % b);
}

// LCM using GCD
int lcm(int a, int b) {
    if (a == 0 || b == 0) return 0;
    return (abs(a) / gcdIterative(a, b)) * abs(b);
}

int main() {
    int a = 48, b = 18;
    
    cout << "GCD of " << a << " and " << b << " (iterative): " 
         << gcdIterative(a, b) << endl;
    cout << "GCD of " << a << " and " << b << " (recursive): " 
         << gcdRecursive(a, b) << endl;
    cout << "LCM of " << a << " and " << b << ": " 
         << lcm(a, b) << endl;
    
    return 0;
}
