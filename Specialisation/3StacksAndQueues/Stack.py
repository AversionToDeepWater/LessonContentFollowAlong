"""

THESE ARE THE KEY METHODS REQUIRED FOR A STACK:

push(item): Add an item to the top of the stack.
pop(): Remove and return the item from the top of the stack.
peek(): View the top item without removing it.
is_empty(): Check if the stack is empty.
is_full() (for limited stacks ONLY) - Check if the stack has reached its maximum size.
size(): Get the current number of items in the stack.

"""


class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        """Return a string representation of the stack."""
        if self.is_empty():
            return "Stack is empty."
        else:
            return "[Bottom] " + " -> ".join(map(str, self.stack)) + " [TOP]"

    def push(self, item):
        """Add an item to the top of the stack."""
        self.stack.append(item)

    def pop(self):
        """Remove and return the item from the top of the stack."""
        if not self.is_empty():
            return self.stack.pop()
        else:
            return IndexError("Stack is empty")

    def peek(self):
        """Return the item at the top of the stack without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        else:
            return IndexError("Stack is empty")

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self, stack):
        """Return the number of items in the stack."""
        return len(stack)


myStack = Stack()

myStack.push("Harry Potter 1")
myStack.push("Far from the Madding Crowd")
myStack.push("YOUR NEXT BOOK")

print(myStack)

myStack.pop()

print(myStack)