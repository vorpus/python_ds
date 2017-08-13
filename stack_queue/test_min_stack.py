"""
tests min stack
"""

import unittest
from min_stack import MinStack
from stack import Stack

class TestMinStack(unittest.TestCase):
    def test_init(self):
        test_min_stack = MinStack()
        self.assertIsInstance(test_min_stack, MinStack)
        self.assertIsInstance(test_min_stack.stack, Stack)
        self.assertIsInstance(test_min_stack.min, Stack)

    def test_push(self):
        test_min_stack = MinStack()
        test_min_stack.push(1)
        test_min_stack.push(2)
        test_min_stack.push(3)
        self.assertEqual(test_min_stack.stack.values, [1,2,3])

    def test_push_min(self):
        test_min_stack = MinStack()
        test_min_stack.push(4)
        self.assertEqual(test_min_stack.peek_min(), 4)
        test_min_stack.push(6)
        self.assertEqual(test_min_stack.peek_min(), 4)
        test_min_stack.push(2)
        self.assertEqual(test_min_stack.peek_min(), 2)

    def test_pop(self):
        test_min_stack = MinStack()
        test_min_stack.push(4)
        test_min_stack.push(6)
        test_min_stack.push(2)
        test_min_stack.push(3)
        self.assertEqual(test_min_stack.peek_min(), 2)
        test_min_stack.pop()
        self.assertEqual(test_min_stack.peek_min(), 2)
        test_min_stack.pop()
        self.assertEqual(test_min_stack.peek_min(), 4)
        test_min_stack.pop()
        self.assertEqual(test_min_stack.peek_min(), 4)
        test_min_stack.pop()
        self.assertEqual(test_min_stack.peek_min(), None)




def main():
    unittest.main()

if __name__ == '__main__':
    main()
