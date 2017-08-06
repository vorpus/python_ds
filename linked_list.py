"""Linked List

Making some python data structures
"""
class LinkedList(object):
    """Linked list class

    Attributes:
        head (LinkedListNode|None): start of linked list
    """
    def __init__(self):
        self.head = None

    # def add(self, val):


class LinkedListNode(object):
    """Node class

    Attributes:
        value (object): item to store in node
        next (LinkedListNode|None): following node
    """
    def __init__(self, value):
        self.value = value
        self.next = None

def main():
    """Run examples"""
    test_node = LinkedListNode(4)

if __name__ == '__main__':
    main()
