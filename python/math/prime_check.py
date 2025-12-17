"""
Prime Number Check Algorithms
Time Complexity: O(sqrt(n)) for is_prime, O(n log log n) for Sieve
Space Complexity: O(1) for is_prime, O(n) for Sieve
"""

def is_prime(n):
    """
    Check if a number is prime
    
    Args:
        n: Integer to check
    
    Returns:
        True if n is prime, False otherwise
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check from 5 to sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sieve_of_eratosthenes(n):
    """
    Find all prime numbers up to n using Sieve of Eratosthenes
    
    Args:
        n: Upper limit
    
    Returns:
        List of all prime numbers up to n
    """
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    primes = [p for p in range(n + 1) if prime[p]]
    return primes

if __name__ == "__main__":
    num = 29
    
    if is_prime(num):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
    
    print("\nPrime numbers up to 50:")
    primes = sieve_of_eratosthenes(50)
    print(primes)
