# 190. Reverse Bits
# https://leetcode.com/problems/reverse-bits/description/


class Solution:
    # Time Cx: O(1), Space Cx: O(1)
    def reverseBits(self, n: int) -> int:
        r = 0
        for i in range(32):
            lsb = n & 1
            r = (r << 1) | lsb
            n >>= 1
        return r


sol = Solution()
n = 3
res = sol.reverseBits(n)
print(res)
