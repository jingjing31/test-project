#include <iostream>
#include <vector>
using namespace std;

// Stack Implementation using Vector
// Time Complexity: O(1) for all operations
// Space Complexity: O(n)

class Stack {
private:
    vector<int> data;
    
public:
    // Push element to stack
    void push(int value) {
        data.push_back(value);
    }
    
    // Pop element from stack
    int pop() {
        if (isEmpty()) {
            cout << "Stack underflow!" << endl;
            return -1;
        }
        int value = data.back();
        data.pop_back();
        return value;
    }
    
    // Get top element
    int top() {
        if (isEmpty()) {
            cout << "Stack is empty!" << endl;
            return -1;
        }
        return data.back();
    }
    
    // Check if stack is empty
    bool isEmpty() {
        return data.empty();
    }
    
    // Get stack size
    int size() {
        return data.size();
    }
    
    // Display stack
    void display() {
        if (isEmpty()) {
            cout << "Stack is empty" << endl;
            return;
        }
        cout << "Stack: ";
        for (int i = data.size() - 1; i >= 0; i--) {
            cout << data[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    Stack s;
    
    s.push(10);
    s.push(20);
    s.push(30);
    
    cout << "After pushing 10, 20, 30:" << endl;
    s.display();
    
    cout << "Top element: " << s.top() << endl;
    cout << "Stack size: " << s.size() << endl;
    
    cout << "Popped element: " << s.pop() << endl;
    s.display();
    
    return 0;
}
