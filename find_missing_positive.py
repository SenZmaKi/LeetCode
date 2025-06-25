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
    # - Use the array indices as a mask for numbers existing in the array since
    # the smallest positive integer must follow 1 <= num <= n
    # - For num <= 0 or num >= n set them to n + 1 to put them out of range
    # essentially ignoring them in the second loop
    def firstMissingPositiveCorrect(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            if not (1 <= nums[i] <= n):
                nums[i] = n + 1
        for i in range(n):
            num = abs(nums[i])
            if 1 <= num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1


sol = Solution()
nums = [3, 4, -1, 1]
res = sol.firstMissingPositiveCorrect(nums)
print(res)
