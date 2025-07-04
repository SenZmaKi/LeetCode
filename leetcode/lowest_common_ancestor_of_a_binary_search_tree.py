# 235. Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Medium


# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left: "TreeNode | None " = None
        self.right: "TreeNode | None" = None


class Solution:
    # Time Cx: O(n), Space Cx: O(n)
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def set_has_node(
            root: TreeNode | None, target: TreeNode, has: set[TreeNode]
        ) -> bool:
            if not root:
                return False
            if target == root:
                has.add(root)
                return True
            child_has = set_has_node(root.left, target, has) or set_has_node(
                root.right, target, has
            )
            if child_has:
                has.add(root)
            return child_has

        has_p: set[TreeNode] = set()
        set_has_node(root, p, has_p)
        has_q: set[TreeNode] = set()
        set_has_node(root, q, has_q)

        queue: deque[TreeNode | None] = deque([root])
        lowest = root
        while queue:
            node = queue.popleft()
            if not node or not (node in has_p and node in has_q):
                continue
            lowest = node
            queue.append(node.left)
            queue.append(node.right)
        return lowest

    # Time Cx: O(n), Space Cx: O(1)
    # The trick is that the LCA is the first node where
    # p and q branch of to different subtrees e.g.
    # p is in the left subtree while q is in the right subtree
    # as opposed to both being in the maybe the left subtree
    def lowestCommonAncestorCorrect(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        curr: TreeNode = root
        while curr:
            if max(p.val, q.val) < curr.val:
                if not curr.left:
                    raise ValueError("No LCA")
                curr = curr.left
            elif min(p.val, q.val) > curr.val:
                if not curr.right:
                    raise ValueError("No LCA")
                curr = curr.right
            else:
                break
        return curr
