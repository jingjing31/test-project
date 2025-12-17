#include <iostream>
#include <queue>
using namespace std;

// Queue Implementation using STL
// Time Complexity: O(1) for all operations
// Space Complexity: O(n)

class Queue {
private:
    queue<int> data;
    
public:
    // Enqueue element to queue
    void enqueue(int value) {
        data.push(value);
    }
    
    // Dequeue element from queue
    int dequeue() {
        if (isEmpty()) {
            cout << "Queue underflow!" << endl;
            return -1;
        }
        int value = data.front();
        data.pop();
        return value;
    }
    
    // Get front element
    int front() {
        if (isEmpty()) {
            cout << "Queue is empty!" << endl;
            return -1;
        }
        return data.front();
    }
    
    // Check if queue is empty
    bool isEmpty() {
        return data.empty();
    }
    
    // Get queue size
    int size() {
        return data.size();
    }
    
    // Display queue (note: STL queue doesn't support iteration)
    void display() {
        if (isEmpty()) {
            cout << "Queue is empty" << endl;
            return;
        }
        queue<int> temp = data;
        cout << "Queue: ";
        while (!temp.empty()) {
            cout << temp.front() << " ";
            temp.pop();
        }
        cout << endl;
    }
};

int main() {
    Queue q;
    
    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);
    
    cout << "After enqueuing 10, 20, 30:" << endl;
    q.display();
    
    cout << "Front element: " << q.front() << endl;
    cout << "Queue size: " << q.size() << endl;
    
    cout << "Dequeued element: " << q.dequeue() << endl;
    q.display();
    
    return 0;
}
