from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()
        
    def enqueue(self, value):
        self.buffer.appendleft(value)
        
    def dequeue(self):
        self.buffer.popleft()
    
    def peek(self):
        return self.buffer[-1]
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    

q = Queue()
q.enqueue(5)
q.enqueue(2)
q.enqueue(9)
q.enqueue(23)
q.enqueue(8)

print(q.buffer)

q.dequeue()
print(q.buffer)