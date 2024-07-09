# Python Data Structures and Algorithms

This repository contains implementations of various data structures and algorithms in Python, including Stack, Queue, Hash Table, Tree, Linked List, Linear Search, Binary Search, and Bubble Sort.

## Table of Contents

- [Data Structures](#data-structures)
  - [Stack](#stack)
  - [Queue](#queue)
  - [Hash Table](#hash-table)
  - [Tree](#tree)
  - [Linked List](#linked-list)
- [Algorithms](#algorithms)
  - [Linear Search](#linear-search)
  - [Binary Search](#binary-search)
  - [Bubble Sort](#bubble-sort)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Data Structures

### Stack
A stack is a linear data structure that follows the Last In First Out (LIFO) principle. The operations include `push`, `pop`, and `peek`.

### Queue
A queue is a linear data structure that follows the First In First Out (FIFO) principle. The operations include `enqueue` and `dequeue`.

### Hash Table
A hash table is a data structure that maps keys to values for highly efficient lookup. It uses a hash function to compute an index into an array of buckets or slots.

### Tree
A tree is a hierarchical data structure with a root node and child nodes, represented by the `TreeNode` class.

### Linked List
A linked list is a linear data structure where each element is a separate object, represented by the `ListNode` class. Each node contains data and a reference to the next node in the sequence.

## Algorithms

### Linear Search
Linear search is a simple search algorithm that checks every element in the list until the target element is found or the list ends.

### Binary Search
Binary search is an efficient search algorithm that works on sorted lists. It repeatedly divides the search interval in half until the target value is found or the interval is empty.

### Bubble Sort
Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

## Installation

To use this repository, clone it to your local machine using:

```bash
git clone https://github.com/imustitanveer/Data_Structures_in_Python.git
```

## Usage

Each data structure and algorithm is implemented in its own Python file. You can import and use them in your own projects as needed. For example, to use the `Stack` class:

```python
from stack import Stack

# Create a new stack
stack = Stack()

# Push elements to the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Pop an element from the stack
print(stack.pop())  # Output: 3
```

## Contributing

Contributions are welcome! If you have any improvements or additional implementations, please open an issue or create a pull request.
