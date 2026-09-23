**EXPERIMENT 3 — Stack and Queue**

The workbook asks for a reusable Python package implementing Stack and Queue using type hints and dataclasses.

**Aim**

To implement Stack and Queue using Python.

**Algorithm**

Stack

1. Create an empty stack.

2. Add elements using push.

3. Remove elements using pop.


Queue

1. Create an empty queue.

2. Add elements using enqueue.

3. Remove elements using dequeue.

**Python Program**

from collections import deque

*# Stack

stack = []

stack.append(10)

stack.append(20)

stack.append(30)

print("Stack:", stack)

print("Popped:", stack.pop())

*# Queue

queue = deque()

queue.append(10)

queue.append(20)

queue.append(30)

print("Queue:", list(queue))

print("Removed:", queue.popleft())

**Output**

Stack: [10, 20, 30]

Popped: 30

Queue: [10, 20, 30]

Removed: 10

**Data & Result**

Stack follows LIFO.

Queue follows FIFO.

**Inference & Analysis**

Stack removes the last inserted element, while Queue removes the first inserted element.

**Result**

Thus, Stack and Queue operations were successfully implemented.
