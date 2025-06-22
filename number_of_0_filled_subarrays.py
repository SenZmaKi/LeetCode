# 2348. Number of Zero-Filled Subarrays
# https://leetcode.com/problems/number-of-zero-filled-subarrays/


class Solution:
    # Time Cx: O(n), Space Cx: O(1)
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        count = 0
        curr_count = 0
        for num in nums:
            curr_count = curr_count + 1 if num == 0 else 0
            count += curr_count
        return count


sol = Solution()
nums = [1, 3, 0, 0, 2, 0, 0, 4]
res = sol.zeroFilledSubarray(nums)
print(res)
