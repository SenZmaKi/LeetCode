# 1512. Number of Good Pairs
# https://leetcode.com/problems/number-of-good-pairs/
from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count: defaultdict[int, int] = defaultdict(int)
        pairs_count = 0
        for num in nums:
            pairs_count += count[num]
            count[num] += 1
        return pairs_count


sol = Solution()
nums = [1, 1]
res = sol.numIdenticalPairs(nums)
print(res)
