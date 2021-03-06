"""Stacks and Queues
More python data structures
"""

class Stack(object):
    def __init__(self):
        self.values = []

    def push(self, val):
        self.values.append(val)

    def pop(self):
        return self.values.pop()

    def peek(self):
        if len(self.values) == 0:
            return None
        return self.values[len(self.values) - 1]

class Queue(object):
    def __init__(self):
        self.values = []

    def enqueue(self, val):
        self.values.append(val)

    def dequeue(self):
        return self.values.pop(0)
