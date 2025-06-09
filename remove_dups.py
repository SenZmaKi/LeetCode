# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/


class Solution:
    # Two pointers problem
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[left] != nums[right]:
                nums[left + 1] = nums[right]
                left += 1

        return left + 1


sol = Solution()
nums = [1, 1]
dup_idx = sol.removeDuplicates(nums)
print(dup_idx)
print(nums[0:dup_idx])
