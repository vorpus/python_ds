"""
tree in python
"""

class BSTNode(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def append(self, node):
        if node.value < self.value:
            if self.left is None:
                self.left = node
            else:
                self.left.append(node)
        else:
            if self.right is None:
                self.right = node
            else:
                self.right.append(node)


class Tree(object):
    def __init__(self):
        self.head = None

    def add(self, val):
        if self.head is not None:
            if isinstance(val, BSTNode):
                self.head.append(val)
            else:
                self.head.append(BSTNode(val))
        else:
            if isinstance(val, BSTNode):
                self.head = val
            else:
                self.head = BSTNode(val)
