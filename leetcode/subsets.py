# 78. Subsets
# https://leetcode.com/problems/subsets/
# Medium


class Solution:
    # Time Cx: O(2^n), Space Cx: O(2^n) for output, O(n) extra space
    def subsets(self, nums: list[int]) -> list[list[int]]:
        visited: set[tuple[int, ...]] = set()

        def explore(curr: tuple[int, ...], start: int) -> None:
            visited.add(curr)
            for index in range(start, len(nums)):
                new = (*curr, nums[index])
                if new not in visited:
                    explore(new, index + 1)

        explore((), 0)
        return [list(comb) for comb in visited]

    # Time Cx: O(2^n), Space Cx: O(2^n) for output, O(n) extra space
    # https://chatgpt.com/s/t_686b4a4491dc8191a88304fc45e6bb4b
    def subsetsDfs(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        subset: list[int] = []

        def dfs(index: int) -> None:
            if index >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[index])
            dfs(index + 1)
            subset.pop()
            dfs(index + 1)

        dfs(0)
        return res

    # Time Cx: O(2^n), Space Cx: O(2^n) for output, O(n) extra space
    def subsetsIterative(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = [[]]
        for num in nums:
            res.extend([[*subset, num] for subset in res])
        return res


sol = Solution()
nums = [1, 2, 3]
res = sol.subsetsIterative(nums)
print(res)
