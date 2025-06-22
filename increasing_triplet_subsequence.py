# 334. Increasing Triplet Subsequence
# https://leetcode.com/problems/increasing-triplet-subsequence/description/


class Solution:
    # Time Cx: O(n), Space Cx: O(1)
    # Two pointers
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = float("inf")
        second = float("inf")
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False


sol = Solution()
nums = [300, 100, 1000, 300, 700]
res = sol.increasingTriplet(nums)
print(res)
