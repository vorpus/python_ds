"""
Tests for tree
"""

import unittest
from tree import BSTNode
from tree import Tree

class TestBSTNode(unittest.TestCase):
    def test_init(self):
        test_node = BSTNode(5)
        self.assertEqual(test_node.value, 5)

    def test_append(self):
        test_node = BSTNode(5)
        test_node.append(BSTNode(3))
        self.assertEqual(test_node.left.value, 3)
        self.assertEqual(test_node.right, None)

    def test_append_multi(self):
        test_node = BSTNode(5)
        test_node.append(BSTNode(3))
        test_node.append(BSTNode(1))
        test_node.append(BSTNode(4))
        self.assertEqual(test_node.left.right.value, 4)
        self.assertEqual(test_node.left.left.value, 1)

class TestTree(unittest.TestCase):
    def test_init(self):
        test_tree = Tree()
        self.assertEqual(test_tree.head, None)

    def test_add(self):
        test_tree = Tree()
        test_tree.add(5)
        self.assertIsInstance(test_tree.head, BSTNode)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
