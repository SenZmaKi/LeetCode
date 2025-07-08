# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/
# Easy


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: "ListNode | None" = None


class Solution:
    # Time Cx: O(n), Space Cx: O(n)
    def hasCycle(self, head: ListNode | None) -> bool:
        visited: set[ListNode] = set()
        curr = head
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next
        return False

    # Time Cx: O(n), Space Cx: O(1)
    # Floyd's Cycle Detection Algorithm
    def hasCycleFloyd(self, head: ListNode | None) -> bool:
        hare = head
        tortoise = head
        while hare and hare.next and tortoise:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return True

        return False
