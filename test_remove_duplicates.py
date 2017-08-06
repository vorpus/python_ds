"""
Write code to remove duplicates from your linked list
"""

import unittest
from linked_list import LinkedList

class TestRemoveDups(unittest.TestCase):
    def test_remove_dups(self):
        ll_with_dups = LinkedList()
        ll_with_dups.append(2)
        ll_with_dups.append(3)
        ll_with_dups.append(2)
        ll_with_dups.append(5)
        ll_with_dups.append(6)
        ll_with_dups.append(1)
        ll_with_dups.append(2)
        ll_with_dups.append(2)
        self.assertEqual(ll_with_dups.length(), 8)
        self.assertEqual(ll_with_dups.to_s(), '2 3 2 5 6 1 2 2')
        ll_with_dups.remove_dups()
        self.assertEqual(ll_with_dups.length(), 5)
        self.assertEqual(ll_with_dups.to_s(), '2 3 5 6 1')

    def test_remove_dups_no_buffer_t(self):
        ll_with_dups = LinkedList()
        ll_with_dups.append(2)
        ll_with_dups.append(2)
        ll_with_dups.append(2)
        ll_with_dups.remove_dups_no_buffer()
        self.assertEqual(ll_with_dups.to_s(), '2')


def main():
    unittest.main()

if __name__ == '__main__':
    main()
