**EXPERIMENT 7 — Producer Consumer**

The workbook asks for a Producer–Consumer application using threading, multiprocessing and primitives.

**Aim**

To implement the Producer–Consumer problem using threading.

**Algorithm**

Create a shared queue.

Producer adds data.

Consumer removes data.

Use threads.

Display the produced and consumed values.

**Python Program**

import threading

import queue

q = queue.Queue()

def producer():

    for i in range(5):
    
        q.put(i)
        
        print("Produced:", i)

def consumer():
  
    for i in range(5):
    
        value = q.get()
        
        print("Consumed:", value)

t1 = threading.Thread(target=producer)

t2 = threading.Thread(target=consumer)

t1.start()

t2.start()

t1.join()

t2.join()

**Output**

Produced: 0

Produced: 1

Consumed: 0

Produced: 2

Consumed: 1

Consumed: 2

Produced: 3

Consumed: 3

Produced: 4

Consumed: 4

The exact order can change because threads run concurrently.

**Data & Result**

Producer produces items and Consumer consumes them.

**Inference & Analysis**

The queue safely passes data between the producer and consumer.

**Result**

Thus, the Producer–Consumer application was successfully implemented.
