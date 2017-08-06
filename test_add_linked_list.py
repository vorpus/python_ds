"""
Add two linked lists, reverse order etc
"""

import unittest
from linked_list import LinkedList

class TestAddLinkedList(unittest.TestCase):
    def test_add_linked_list(self):
        ll1 = LinkedList()
        ll1.append(3)
        ll1.append(1)
        ll1.append(5)
        ll2 = LinkedList()
        ll2.append(5)
        ll2.append(9)
        ll2.append(2)
        self.assertEqual(LinkedList.add_linked_list(ll1, ll2).to_s(), '8 0 8')
        ll2.append(3)
        self.assertEqual(LinkedList.add_linked_list(ll1, ll2).to_s(), '8 0 8 3')
        ll1.append(1)
        ll1.append(1)
        ll1.append(1)
        ll1.append(1)
        self.assertEqual(LinkedList.add_linked_list(ll1, ll2).to_s(), '8 0 8 4 1 1 1')


def main():
    unittest.main()

if __name__ == '__main__':
    main()
