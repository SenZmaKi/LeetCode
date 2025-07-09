# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# Medium


class Solution:
    # Time Cx: O(n), Space Cx: O(1)
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0

        def calc_area() -> int:
            h = min(height[left], height[right])
            w = right - left
            return h * w

        while left < right:
            area = calc_area()
            res = max(area, res)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return res


sol = Solution()
height = [1, 2, 4, 3]
res = sol.maxArea(height)
print(res)
