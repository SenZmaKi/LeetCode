# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/
# Easy


# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time Cx: O(n), Space Cx: O(n)
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    # Time Cx: O(n), Space Cx: O(n)
    def invertTreeBfs(self, root: TreeNode | None) -> TreeNode | None:
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                continue
            node.left, node.right = node.right, node.left
            q.append(node.right)
            q.append(node.left)
        return root
