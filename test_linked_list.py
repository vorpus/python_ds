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

def main():
  unittest.main()

if __name__ == '__main__':
  main()
