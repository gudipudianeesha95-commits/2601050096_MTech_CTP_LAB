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