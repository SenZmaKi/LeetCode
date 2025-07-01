# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/description/


class Solution:
    # Time Cx: O(log n), Space Cx: O(1)
    def hammingWeight(self, n: int) -> int:
        weight = 0
        while n >= 1:
            rem = n % 2
            if rem:
                weight += 1
            n //= 2
        return weight

    # Time Cx: O(1), Space Cx: O(1)
    def hammingWeightCorrect(self, n) -> int:
        res = 0
        # Question constrains n to be a 32 bit unsigned integer
        for i in range(32):
            if (n >> i) & 1:
                res += 1
        return res


sol = Solution()
n = 122
res = sol.hammingWeight(n)
print(res)
