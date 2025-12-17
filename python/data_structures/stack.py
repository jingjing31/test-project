"""
Stack Implementation
Time Complexity: O(1) for all operations
Space Complexity: O(n)
"""

class Stack:
    """Stack data structure implementation using list"""
    
    def __init__(self):
        """Initialize empty stack"""
        self.data = []
    
    def push(self, value):
        """
        Push element to stack
        
        Args:
            value: Element to push
        """
        self.data.append(value)
    
    def pop(self):
        """
        Pop element from stack
        
        Returns:
            Top element, or None if stack is empty
        """
        if self.is_empty():
            print("Stack underflow!")
            return None
        return self.data.pop()
    
    def top(self):
        """
        Get top element without removing it
        
        Returns:
            Top element, or None if stack is empty
        """
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.data[-1]
    
    def is_empty(self):
        """
        Check if stack is empty
        
        Returns:
            True if stack is empty, False otherwise
        """
        return len(self.data) == 0
    
    def size(self):
        """
        Get stack size
        
        Returns:
            Number of elements in stack
        """
        return len(self.data)
    
    def display(self):
        """Display stack contents"""
        if self.is_empty():
            print("Stack is empty")
            return
        print("Stack:", " ".join(map(str, reversed(self.data))))

if __name__ == "__main__":
    s = Stack()
    
    s.push(10)
    s.push(20)
    s.push(30)
    
    print("After pushing 10, 20, 30:")
    s.display()
    
    print(f"Top element: {s.top()}")
    print(f"Stack size: {s.size()}")
    
    print(f"Popped element: {s.pop()}")
    s.display()
