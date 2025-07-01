# 1. Two Sum
# https://leetcode.com/problems/two-sum/description/


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}
        for index, num in enumerate(nums):
            rem = target - num
            other = seen.get(rem, None)
            if other is not None:
                return [other, index]
            seen[num] = index
        print(seen)
        raise ValueError("No two sum pair found in:", nums)


sol = Solution()
nums = [2, 7, 11, 15]
target = 9
res = sol.twoSum(nums, target)
print(res)
