# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/description/


class Solution:
    # Time Cx: O(n), Space Cx: O(1)
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = nums[0]
        currentSum = nums[0]
        for i in range(1, len(nums)):
            currentSum = max(nums[i], nums[i] + currentSum)
            maxSum = max(currentSum, maxSum)
        return maxSum


sol = Solution()
nums = [1, 2, 3]
res = sol.maxSubArray(nums)
print(res)
