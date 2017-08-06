"""
Write code to find the nth to last element of a linked list
"""

import unittest
from linked_list import LinkedList

class TestNthToLast(unittest.TestCase):
    def test_nth_to_last(self):
        ll_with_dups = LinkedList()
        ll_with_dups.append(2)
        ll_with_dups.append(3)
        ll_with_dups.append(2)
        ll_with_dups.append(5)
        ll_with_dups.append(6)
        ll_with_dups.append(1)
        ll_with_dups.append(2)
        ll_with_dups.append(999)
        self.assertEqual(ll_with_dups.nth_to_last(2).value, 1)
        self.assertEqual(ll_with_dups.nth_to_last(3).value, 6)
        self.assertEqual(ll_with_dups.nth_to_last(0).value, 999)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
