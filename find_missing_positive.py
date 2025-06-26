# 41. First Missing Positive
# https://leetcode.com/problems/first-missing-positive/


class Solution:
    # Time Cx: O(n log n), Space CX: O(1)
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums.sort()
        next_ = 1
        for num in nums:
            if num == next_:
                next_ += 1
            if num > next_:
                return next_
        return next_

    # Time Cx: O(n), Space CX: O(1)
    #
    # 1. Iterate over the array and place every number num at index num - 1
    #    if it is within the array bounds (i.e., 1 <= num <= n).
    # 2. Once all numbers are placed, iterate over the array.
    # 3. The first index where nums[i] is not i + 1 gives the missing positive integer.
    # 4. If all indices are correct, the missing integer is n + 1.
    #
    # The core idea is to use the array indices as a mask for numbers existing in the array
    def firstMissingPositiveCorrect(self, nums: list[int]):
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap numbers to their correct position.
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # If after rearrangement, nums[i] != i + 1, i + 1 is the missing number.
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all numbers are in their correct positions, the missing number is n+1
        return n + 1


sol = Solution()
nums = [3, 4, -1, 1]
res = sol.firstMissingPositiveCorrect(nums)
print(res)
