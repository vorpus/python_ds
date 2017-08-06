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

    def to_s(self):
        to_str = ''
        node = self.head
        while node:
            to_str += str(node.value)
            if node.next:
                to_str += ' '
            node = node.next
        return to_str

    def get_tail(self):
        node = self.head
        while node.next:
            node = node.next
        return node

    def length(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

    def remove_dups(self):
        dups = set()
        node = self.head
        dups.add(node.value)
        while node.next:
            if node.next.value in dups:
                node.next = node.next.next
            else:
                node = node.next

    def remove_dups_no_buffer(self):
        node1 = self.head
        while node1:
            node2 = node1
            while node2:
                while node2.next:
                    if node2.next.value == node1.value:
                        node2.next = node2.next.next
                node2 = node2.next
            node1 = node1.next

    def nth_to_last(self, n):
        current_node = self.head
        nth_node = current_node
        for _ in range(0, n):
            if nth_node:
                nth_node = nth_node.next
            else:
                return None
        while nth_node.next:
            current_node = current_node.next
            nth_node = nth_node.next
        return current_node

    @staticmethod
    def add_linked_list(list1, list2):
        node1 = list1.head
        node2 = list2.head
        new_list = None
        new_list_last = None
        carry = 0
        while node1 and node2:
            new_node_value = (carry + node1.value + node2.value)
            carry = 0
            if new_node_value >= 10:
                carry = 1
                new_node_value = new_node_value % 10
            if new_list:
                new_list_last.next = LinkedListNode(new_node_value)
                new_list_last = new_list_last.next
            else:
                new_list = LinkedListNode(new_node_value)
                new_list_last = new_list
            node1 = node1.next
            node2 = node2.next
        new_list_last.next = node1 or node2
        return new_list


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

    def to_s(self):
        to_str = ''
        node = self
        while node:
            to_str += str(node.value)
            if node.next:
                to_str += ' '
            node = node.next
        return to_str


    def delete_next(self):
        if self.next:
            if self.next.next:
                self.next = self.next.next
            else:
                self.next = None
