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

    def append(self, val):
        if self.head:
            self.head.append(val)
        else:
            if isinstance(val, LinkedListNode):
                self.head = val
            else:
                self.head = LinkedListNode(val)

    def get_tail(self):
        head = self.head
        while head.next:
            head = head.next
        return head


class LinkedListNode(object):
    """Node class

    Attributes:
        value (object): item to store in node
        next (LinkedListNode|None): following node
    """
    def __init__(self, value):
        self.value = value
        self.next = None

    def append(self, value):
        if self.next:
            self.next.append(value)
        else:
            if isinstance(value, LinkedListNode):
                self.next = value
            else:
                self.next = LinkedListNode(value)

def main():
    """Run examples"""
    test_node = LinkedListNode(4)

if __name__ == '__main__':
    main()
