"""
Singly Linked List Implementation
Time Complexity: O(1) for insertion at head, O(n) for others
Space Complexity: O(n)
"""

class Node:
    """Node class for linked list"""
    
    def __init__(self, data):
        """
        Initialize a node
        
        Args:
            data: Value to store in node
        """
        self.data = data
        self.next = None

class LinkedList:
    """Singly Linked List implementation"""
    
    def __init__(self):
        """Initialize empty linked list"""
        self.head = None
    
    def insert_at_beginning(self, value):
        """
        Insert at beginning of list
        
        Args:
            value: Value to insert
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, value):
        """
        Insert at end of list
        
        Args:
            value: Value to insert
        """
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
    
    def delete_node(self, value):
        """
        Delete node with given value
        
        Args:
            value: Value to delete
        """
        if self.head is None:
            return
        
        if self.head.data == value:
            self.head = self.head.next
            return
        
        temp = self.head
        while temp.next is not None and temp.next.data != value:
            temp = temp.next
        
        if temp.next is not None:
            temp.next = temp.next.next
    
    def search(self, value):
        """
        Search for a value in list
        
        Args:
            value: Value to search for
        
        Returns:
            True if found, False otherwise
        """
        temp = self.head
        while temp is not None:
            if temp.data == value:
                return True
            temp = temp.next
        return False
    
    def display(self):
        """Display linked list"""
        if self.head is None:
            print("List is empty")
            return
        
        temp = self.head
        elements = []
        while temp is not None:
            elements.append(str(temp.data))
            temp = temp.next
        print("List:", " -> ".join(elements) + " -> NULL")

if __name__ == "__main__":
    list = LinkedList()
    
    list.insert_at_end(10)
    list.insert_at_end(20)
    list.insert_at_end(30)
    list.insert_at_beginning(5)
    
    print("After insertions:")
    list.display()
    
    print(f"Searching for 20: {'Found' if list.search(20) else 'Not found'}")
    
    list.delete_node(20)
    print("After deleting 20:")
    list.display()
