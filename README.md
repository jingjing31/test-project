# Basic Algorithms Collection - 2025.12.17

A comprehensive collection of fundamental algorithms implemented in both **C++** and **Python**. This repository serves as a reference for common algorithms used in computer science and software development.

## Table of Contents

- [Sorting Algorithms](#sorting-algorithms)
- [Searching Algorithms](#searching-algorithms)
- [Mathematical Algorithms](#mathematical-algorithms)
- [Data Structures](#data-structures)
- [How to Run](#how-to-run)

---

## Sorting Algorithms

### 1. Bubble Sort
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1)
- **Description**: Repeatedly steps through the list, compares adjacent elements and swaps them if they are in wrong order.
- **Files**:
  - C++: `cpp/sorting/bubble_sort.cpp`
  - Python: `python/sorting/bubble_sort.py`

### 2. Selection Sort
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1)
- **Description**: Divides the list into sorted and unsorted regions, repeatedly selects the minimum element from unsorted region.
- **Files**:
  - C++: `cpp/sorting/selection_sort.cpp`
  - Python: `python/sorting/selection_sort.py`

### 3. Insertion Sort
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1)
- **Description**: Builds the final sorted array one item at a time by inserting each element into its proper position.
- **Files**:
  - C++: `cpp/sorting/insertion_sort.cpp`
  - Python: `python/sorting/insertion_sort.py`

### 4. Merge Sort
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)
- **Description**: Divide and conquer algorithm that divides the array into halves, sorts them, and merges them back.
- **Files**:
  - C++: `cpp/sorting/merge_sort.cpp`
  - Python: `python/sorting/merge_sort.py`

### 5. Quick Sort
- **Time Complexity**: O(n log n) average, O(n²) worst case
- **Space Complexity**: O(log n)
- **Description**: Divide and conquer algorithm that picks a pivot element and partitions the array around it.
- **Files**:
  - C++: `cpp/sorting/quick_sort.cpp`
  - Python: `python/sorting/quick_sort.py`

---

## Searching Algorithms

### 1. Linear Search
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Description**: Sequentially checks each element of the list until a match is found.
- **Files**:
  - C++: `cpp/searching/linear_search.cpp`
  - Python: `python/searching/linear_search.py`

### 2. Binary Search
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1) iterative, O(log n) recursive
- **Description**: Efficiently searches a sorted array by repeatedly dividing the search interval in half.
- **Files**:
  - C++: `cpp/searching/binary_search.cpp`
  - Python: `python/searching/binary_search.py`

---

## Mathematical Algorithms

### 1. Factorial
- **Time Complexity**: O(n)
- **Space Complexity**: O(1) iterative, O(n) recursive
- **Description**: Calculates the product of all positive integers less than or equal to n.
- **Files**:
  - C++: `cpp/math/factorial.cpp`
  - Python: `python/math/factorial.py`

### 2. Fibonacci
- **Time Complexity**: O(n) for iterative/DP, O(2ⁿ) for naive recursive
- **Space Complexity**: O(1) iterative, O(n) for DP/recursive
- **Description**: Generates the Fibonacci sequence where each number is the sum of the two preceding ones.
- **Files**:
  - C++: `cpp/math/fibonacci.cpp`
  - Python: `python/math/fibonacci.py`

### 3. GCD and LCM
- **Time Complexity**: O(log(min(a,b)))
- **Space Complexity**: O(1) iterative, O(log(min(a,b))) recursive
- **Description**: Calculates Greatest Common Divisor and Least Common Multiple using Euclidean algorithm.
- **Files**:
  - C++: `cpp/math/gcd_lcm.cpp`
  - Python: `python/math/gcd_lcm.py`

### 4. Prime Number Check
- **Time Complexity**: O(√n) for primality test, O(n log log n) for Sieve
- **Space Complexity**: O(1) for primality test, O(n) for Sieve
- **Description**: Checks if a number is prime and generates all primes up to n using Sieve of Eratosthenes.
- **Files**:
  - C++: `cpp/math/prime_check.cpp`
  - Python: `python/math/prime_check.py`

---

## Data Structures

### 1. Stack
- **Time Complexity**: O(1) for all operations
- **Space Complexity**: O(n)
- **Description**: LIFO (Last In First Out) data structure with push, pop, and top operations.
- **Files**:
  - C++: `cpp/data_structures/stack.cpp`
  - Python: `python/data_structures/stack.py`

### 2. Queue
- **Time Complexity**: O(1) for all operations
- **Space Complexity**: O(n)
- **Description**: FIFO (First In First Out) data structure with enqueue and dequeue operations.
- **Files**:
  - C++: `cpp/data_structures/queue.cpp`
  - Python: `python/data_structures/queue.py`

### 3. Linked List
- **Time Complexity**: O(1) for insertion at head, O(n) for other operations
- **Space Complexity**: O(n)
- **Description**: Linear data structure where elements are stored in nodes with pointers to the next node.
- **Files**:
  - C++: `cpp/data_structures/linked_list.cpp`
  - Python: `python/data_structures/linked_list.py`

---

## How to Run

### C++ Programs

1. Compile the program:
```bash
g++ -o output_name cpp/category/algorithm_name.cpp
```

2. Run the compiled program:
```bash
./output_name
```

**Example**:
```bash
g++ -o bubble_sort cpp/sorting/bubble_sort.cpp
./bubble_sort
```

### Python Programs

Run the Python script directly:
```bash
python3 python/category/algorithm_name.py
```

**Example**:
```bash
python3 python/sorting/bubble_sort.py
```

---

## Directory Structure

```
.
├── cpp/
│   ├── sorting/
│   │   ├── bubble_sort.cpp
│   │   ├── selection_sort.cpp
│   │   ├── insertion_sort.cpp
│   │   ├── merge_sort.cpp
│   │   └── quick_sort.cpp
│   ├── searching/
│   │   ├── linear_search.cpp
│   │   └── binary_search.cpp
│   ├── math/
│   │   ├── factorial.cpp
│   │   ├── fibonacci.cpp
│   │   ├── gcd_lcm.cpp
│   │   └── prime_check.cpp
│   └── data_structures/
│       ├── stack.cpp
│       ├── queue.cpp
│       └── linked_list.cpp
└── python/
    ├── sorting/
    │   ├── bubble_sort.py
    │   ├── selection_sort.py
    │   ├── insertion_sort.py
    │   ├── merge_sort.py
    │   └── quick_sort.py
    ├── searching/
    │   ├── linear_search.py
    │   └── binary_search.py
    ├── math/
    │   ├── factorial.py
    │   ├── fibonacci.py
    │   ├── gcd_lcm.py
    │   └── prime_check.py
    └── data_structures/
        ├── stack.py
        ├── queue.py
        └── linked_list.py
```

---

## Contributing

Feel free to contribute by:
- Adding new algorithms
- Improving existing implementations
- Adding test cases
- Fixing bugs or improving documentation

---

## License

This project is open source and available for educational purposes.
