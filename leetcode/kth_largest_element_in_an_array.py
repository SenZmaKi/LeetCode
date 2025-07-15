# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Medium


import heapq


class Solution:
    # Time Cx: O(n log n), Space Cx: O(n)
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]

    # Time Cx: O(n log n), Space Cx: O(n)
    def findKthLargestHeap(self, nums: list[int], k: int) -> int:
        return heapq.nlargest(k, nums)[k - 1]


sol = Solution()
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
res = sol.findKthLargest(nums, 4)
print(res)
