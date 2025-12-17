#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

// Prime Number Check Algorithms
// Time Complexity: O(sqrt(n)) for isPrime, O(n log log n) for Sieve
// Space Complexity: O(1) for isPrime, O(n) for Sieve

// Check if a number is prime
bool isPrime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    
    // Check from 5 to sqrt(n)
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    }
    return true;
}

// Sieve of Eratosthenes - find all primes up to n
vector<int> sieveOfEratosthenes(int n) {
    vector<bool> prime(n + 1, true);
    vector<int> primes;
    
    prime[0] = prime[1] = false;
    
    for (int p = 2; p * p <= n; p++) {
        if (prime[p]) {
            for (int i = p * p; i <= n; i += p) {
                prime[i] = false;
            }
        }
    }
    
    for (int p = 2; p <= n; p++) {
        if (prime[p]) {
            primes.push_back(p);
        }
    }
    
    return primes;
}

int main() {
    int num = 29;
    
    if (isPrime(num)) {
        cout << num << " is a prime number" << endl;
    } else {
        cout << num << " is not a prime number" << endl;
    }
    
    cout << "\nPrime numbers up to 50: ";
    vector<int> primes = sieveOfEratosthenes(50);
    for (int prime : primes) {
        cout << prime << " ";
    }
    cout << endl;
    
    return 0;
}
