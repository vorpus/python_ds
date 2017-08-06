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

class TestLinkedList(unittest.TestCase):

    def test_init(self):
        test_list = LinkedList()
        self.assertEqual(test_list.head, None)

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
        self.assertEqual(test_list.head.next.next.value, 2)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
