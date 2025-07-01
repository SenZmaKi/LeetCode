# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# https://neetcode.io/solutions/climbing-stairs


class Solution:
    # Time Cx: O(n), Space Cx: O(n)
    def climbStairs(self, n: int, memo: dict[int, int] = {}) -> int:
        memoed_count = memo.get(n)
        if memoed_count is not None:
            return memoed_count
        if n == 0:
            return 1
        elif n < 0:
            return 0
        distinct_paths_count = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        memo[n] = distinct_paths_count
        return distinct_paths_count

    # Time Cx: O(n), Space Cx: O(n)
    def climbStairsBottomUp(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    # Time Cx: O(n), Space Cx: O(1)
    def climbStairsBottomUpSpaceOptimized(self, n: int) -> int:
        prev1 = 1
        prev2 = 0
        for i in range(n):
            prev1, prev2 = prev1 + prev2, prev1
        return prev1


sol = Solution()
n = 69
res = sol.climbStairsBottomUpSpaceOptimized(n)
print(res)
