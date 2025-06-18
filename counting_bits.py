# 338. Counting Bits
# https://leetcode.com/problems/counting-bits/description/


class Solution:
    # Time Cx: O(n), Space Cx: O(n)
    def countBits(self, n: int) -> list[int]:
        def count_bits(num: int) -> int:
            res = 0
            for i in range(32):
                if (num >> i) & 1:
                    res += 1
            return res

        return [count_bits(num) for num in range(n + 1)]

    # Time Cx: O(n), Space Cx: O(n)
    # Bit manipulation and Dynamic programming
    def countBitsCorrect(self, n: int) -> list[int]:
        dp = [0] * (n + 1)
        base = 1
        for i in range(1, n + 1):
            if (base * 2) == i:
                base = i
            dp[i] = dp[i - base] + 1
        return dp


sol = Solution()
n = 10
res = sol.countBits(n)
print(res)
