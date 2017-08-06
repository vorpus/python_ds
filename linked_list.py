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
        # current_node = self.head
        # while current_node.next:
        #     last_before_dup = current_node
        #     if last_before_dup.next:
        #         next_node = last_before_dup.next
        #         while next_node.value == current_node.value:
        #             last_before_dup.next = next_node.next
        #             next_node = last_before_dup.next
        #             if isinstance(next_node, type(None)):
        #                 break
        #         current_node = current_node.next
        #         if isinstance(current_node, type(None)):
        #             break

    # 2 3 2 5 6 1 2 2

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

    def delete_next(self):
        if self.next:
            if self.next.next:
                self.next = self.next.next
            else:
                self.next = None
