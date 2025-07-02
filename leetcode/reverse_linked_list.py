# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# Easy


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


class Solution:
    # Time Cx: O(n), Space Cx: O(1)
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        curr = head
        prev = None
        while curr is not None:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        return prev

    def reverseListRecursive(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None
        new_head = head
        next_ = head.next
        if next_ is not None:
            new_head = self.reverseListRecursive(next_)
            next_.next = head
        head.next = None
        return new_head
