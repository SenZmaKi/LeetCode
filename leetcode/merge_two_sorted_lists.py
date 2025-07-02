# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
# Easy


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        curr: ListNode | None = None
        head = curr
        while list1 and list2:
            if list1.val < list2.val:
                node = list1
                list1 = list1.next
            else:
                node = list2
                list2 = list2.next
            if not curr:
                head = node
            else:
                curr.next = node
            curr = node
        rem = list1 or list2
        if rem:
            if curr:
                curr.next = rem
            else:
                head = rem
        return head

    def mergeTwoListsClean(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        dummy = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node = list1
                list1 = list1.next
            else:
                node = list2
                list2 = list2.next
            node = node.next

        if node:  # Always true, here for my typechecker to stop complaining
            node.next = list1 or list2
        return dummy.next
