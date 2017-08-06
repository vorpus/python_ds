"""
Unit tests for linked list
"""

import unittest
from linked_list import LinkedList
from linked_list import LinkedListNode

class TestLinkedListNode(unittest.TestCase):

    def test_init(self):
        test_node = LinkedListNode(4)
        self.assertEqual(test_node.value, 4)

    def test_append(self):
        """Can append number"""
        test_list = LinkedList()
        test_list.append(4)
        self.assertEqual(test_list.head.value, 4)

        """Can append node"""
        test_list = LinkedList()
        test_node = LinkedListNode(4)
        test_list.append(test_node)
        self.assertEqual(test_list.head.value, 4)

    def test_multiple_append(self):
        test_list = LinkedList()
        test_node_1 = LinkedListNode(1)
        test_node_2 = LinkedListNode(2)
        test_node_3 = LinkedListNode(3)
        test_list.append(test_node_1)
        test_list.append(test_node_2)
        test_list.append(test_node_3)
        self.assertEqual(test_list.head.value, 1)
        self.assertEqual(test_list.head.next.value, 2)
        self.assertEqual(test_list.head.next.next.value, 3)

    def test_delete_next(self):
        test_node_1 = LinkedListNode(1)
        test_node_1.append(2)
        test_node_1.append(3)
        self.assertEqual(test_node_1.next.value, 2)
        test_node_1.delete_next()
        self.assertEqual(test_node_1.next.value, 3)



class TestLinkedList(unittest.TestCase):

    def test_init(self):
        test_list = LinkedList()
        self.assertEqual(test_list.head, None)

    def test_print(self):
        test_list = LinkedList()
        test_list.append(1)
        test_list.append(2)
        test_list.append(3)
        test_list.append(2)
        self.assertEqual(test_list.to_s(), '1 2 3 2')

    def test_get_tail(self):
        test_list = LinkedList()
        test_node_1 = LinkedListNode(1)
        test_node_2 = LinkedListNode(2)
        test_node_3 = LinkedListNode(3)
        test_list.append(test_node_1)
        test_list.append(test_node_2)
        test_list.append(test_node_3)
        self.assertEqual(test_list.get_tail().value, 3)

    def test_length(self):
        test_list = LinkedList()
        self.assertEqual(test_list.length(), 0)
        test_list.append(4)
        self.assertEqual(test_list.length(), 1)
        test_list.append(4)
        self.assertEqual(test_list.length(), 2)
        test_list.append(4)
        self.assertEqual(test_list.length(), 3)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
