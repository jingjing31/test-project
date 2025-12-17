"""
Factorial Algorithm
Time Complexity: O(n)
Space Complexity: O(1) for iterative, O(n) for recursive
"""

def factorial_iterative(n):
    """
    Calculate factorial using iterative approach
    
    Args:
        n: Non-negative integer
    
    Returns:
        Factorial of n, or None if n is negative
    """
    if n < 0:
        return None  # Error: factorial of negative number
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """
    Calculate factorial using recursive approach
    
    Args:
        n: Non-negative integer
    
    Returns:
        Factorial of n, or None if n is negative
    """
    if n < 0:
        return None  # Error: factorial of negative number
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

if __name__ == "__main__":
    num = 5
    
    print(f"Factorial of {num} (iterative): {factorial_iterative(num)}")
    print(f"Factorial of {num} (recursive): {factorial_recursive(num)}")
