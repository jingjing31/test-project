"""
GCD and LCM Algorithms
Time Complexity: O(log(min(a,b)))
Space Complexity: O(1) for iterative, O(log(min(a,b))) for recursive
"""

def gcd_iterative(a, b):
    """
    Calculate GCD using Euclidean algorithm (iterative)
    
    Args:
        a: First integer
        b: Second integer
    
    Returns:
        Greatest Common Divisor of a and b
    """
    a = abs(a)
    b = abs(b)
    
    while b != 0:
        a, b = b, a % b
    return a

def gcd_recursive(a, b):
    """
    Calculate GCD using Euclidean algorithm (recursive)
    
    Args:
        a: First integer
        b: Second integer
    
    Returns:
        Greatest Common Divisor of a and b
    """
    a = abs(a)
    b = abs(b)
    
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

def lcm(a, b):
    """
    Calculate LCM using GCD
    
    Args:
        a: First integer
        b: Second integer
    
    Returns:
        Least Common Multiple of a and b
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd_iterative(a, b)

if __name__ == "__main__":
    a, b = 48, 18
    
    print(f"GCD of {a} and {b} (iterative): {gcd_iterative(a, b)}")
    print(f"GCD of {a} and {b} (recursive): {gcd_recursive(a, b)}")
    print(f"LCM of {a} and {b}: {lcm(a, b)}")
