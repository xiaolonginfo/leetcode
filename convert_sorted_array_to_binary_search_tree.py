#! /usr/bin/env python
# encoding: utf-8
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        return self._tree(nums, 0, len(nums) - 1)

    def _tree(self, nums, left, right):
        if not nums or left > right:
            return None
        mid = (left + right + 1) / 2
        node = TreeNode(nums[mid])
        node.left = self._tree(nums, left, mid - 1)
        node.right = self._tree(nums, mid + 1, right)
        return node


class BSTCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _tree_to_array(self, node, lst):
        if not node:
            return lst
        # left
        if node.left:
            self._tree_to_array(node.left, lst)
        # root
        lst.append(node.val)
        # right
        if node.right:
            self._tree_to_array(node.right, lst)
        return lst

    def test_BST(self):
        s = Solution()
        for arr, ret in [([], []),
                         ([0], [0]),
                         ([0, 1], [0, 1]),
                         ([0, 1, 2], [0, 1, 2])]:
            tree = s.sortedArrayToBST(arr)
            lst = self._tree_to_array(tree, [])
            self.assertEqual(ret, lst)


if __name__ == '__main__':
    unittest.main()