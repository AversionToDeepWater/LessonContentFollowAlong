"""

THESE ARE THE KEY METHODS REQUIRED FOR A QUEUE:

enqueue(item) - Add an item to the end of the queue.
dequeue() - Remove and return the item from the front of the queue.
peek() - View the front item without removing it.
is_empty() - Check if the queue is empty.
is_full() (for limited queues ONLY) - Check if the queue has reached its maximum size.
size() - Return the number of items in the queue.

"""
class Queue:

    def __init__(self):
        self.queue = []

    def __str__(self):
        return  "[FRONT]" + " -> ".join(map(str, self.queue)) + "[BACK]"

    def enqueue(self, item):
        #Add item to queue
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            #Remove first item from left of list, always return item you are removing
            return self.queue.pop(0)
        else:
            raise IndexError("Dequeue from empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def peak(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Peaking from an empty Queue")

    def size(self):
        return len(self.queue)

q = Queue()

q.enqueue(444)
q.enqueue(777)
q.enqueue(888)
print(q)

print("REMOVING: ", q.dequeue())
print(q)