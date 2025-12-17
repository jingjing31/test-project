"""
Queue Implementation
Time Complexity: O(1) for all operations
Space Complexity: O(n)
"""

from collections import deque

class Queue:
    """Queue data structure implementation using deque"""
    
    def __init__(self):
        """Initialize empty queue"""
        self.data = deque()
    
    def enqueue(self, value):
        """
        Enqueue element to queue
        
        Args:
            value: Element to enqueue
        """
        self.data.append(value)
    
    def dequeue(self):
        """
        Dequeue element from queue
        
        Returns:
            Front element, or None if queue is empty
        """
        if self.is_empty():
            print("Queue underflow!")
            return None
        return self.data.popleft()
    
    def front(self):
        """
        Get front element without removing it
        
        Returns:
            Front element, or None if queue is empty
        """
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.data[0]
    
    def is_empty(self):
        """
        Check if queue is empty
        
        Returns:
            True if queue is empty, False otherwise
        """
        return len(self.data) == 0
    
    def size(self):
        """
        Get queue size
        
        Returns:
            Number of elements in queue
        """
        return len(self.data)
    
    def display(self):
        """Display queue contents"""
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue:", " ".join(map(str, self.data)))

if __name__ == "__main__":
    q = Queue()
    
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    
    print("After enqueuing 10, 20, 30:")
    q.display()
    
    print(f"Front element: {q.front()}")
    print(f"Queue size: {q.size()}")
    
    print(f"Dequeued element: {q.dequeue()}")
    q.display()
