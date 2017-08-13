"""
min stack
"""

from stack import Stack

class MinStack(object):
    def __init__(self):
        self.stack = Stack()
        self.min = Stack()

    def push(self, val):
        self.stack.push(val)
        current_min = self.min.peek()
        if current_min is None or val < current_min:
            self.min.push(val)

    def pop(self):
        val_popped = self.stack.pop()
        if val_popped == self.min.peek():
            self.min.pop()

    def peek_min(self):
        return self.min.peek()
