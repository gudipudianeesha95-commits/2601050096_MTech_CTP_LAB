from collections import deque

# Stack
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)
print("Popped:", stack.pop())

# Queue
queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", list(queue))
print("Removed:", queue.popleft())