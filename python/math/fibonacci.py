"""
Fibonacci Algorithm
Time Complexity: O(n) for iterative and DP, O(2^n) for naive recursive
Space Complexity: O(1) for iterative, O(n) for DP and recursive
"""

def fibonacci_iterative(n):
    """
    Calculate nth Fibonacci number using iterative approach
    
    Args:
        n: Non-negative integer
    
    Returns:
        nth Fibonacci number, or None if n is negative
    """
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursive(n):
    """
    Calculate nth Fibonacci number using recursive approach (naive)
    
    Args:
        n: Non-negative integer
    
    Returns:
        nth Fibonacci number, or None if n is negative
    """
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_dp(n):
    """
    Calculate nth Fibonacci number using dynamic programming
    
    Args:
        n: Non-negative integer
    
    Returns:
        nth Fibonacci number, or None if n is negative
    """
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

if __name__ == "__main__":
    n = 10
    
    print(f"Fibonacci of {n} (iterative): {fibonacci_iterative(n)}")
    print(f"Fibonacci of {n} (recursive): {fibonacci_recursive(n)}")
    print(f"Fibonacci of {n} (DP): {fibonacci_dp(n)}")
