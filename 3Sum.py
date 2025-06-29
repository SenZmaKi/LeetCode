# 15: 3Sum
# https://leetcode.com/problems/3sum/description/


class Solution:
    # Time Cx: O(n^2) Space Cx: O(n) (Cause of timsort)
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        three_sum: list[list[int]] = []
        nums.sort()
        for i in range(len(nums)):
            if i and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    three_sum.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return three_sum


sol = Solution()
nums = [-1, 0, 1, 2, -1, -4]
res = sol.threeSum(nums)
print(res)
