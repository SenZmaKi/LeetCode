# 55. Jump Game
# https://leetcode.com/problems/jump-game/
# Medium


class Solution:
    # Time Cx: O(n^2), Space Cx: O(1)
    # Bottom Up Dynamic Programming
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)

        def explore(index: int) -> bool:
            if index >= n - 1:
                return True
            print(index)
            if nums[index] == -1:
                return False
            for i in reversed(range(1, nums[index] + 1)):
                if explore(index + i):
                    return True
            nums[index] = -1
            return False

        return explore(0)

    # Time Cx: O(n), Space Cx: O(1)
    # Greedy
    def canJumpGreedy(self, nums: list[int]) -> bool:
        n = len(nums)
        goal = n - 1
        for i in range(n - 2, -1, -1):
            full_jump_distance = i + nums[i]
            if full_jump_distance >= goal:
                goal = i
        return goal == 0


sol = Solution()
nums = [2, 3, 1, 1, 4]
res = sol.canJumpGreedy(nums)
print(res)
