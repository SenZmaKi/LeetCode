# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
class Solution:
    def binarySearch(self, target: int, nums: list[int], left: int) -> int | None:
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            num = nums[mid]
            if num == target:
                return mid
            if target > num:
                left = mid + 1
            else:
                right = mid

    # Time Cx: O(n log n), Space Cx: O(1)
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for idx in range(len(numbers)):
            rem = target - numbers[idx]
            other_idx = self.binarySearch(rem, numbers, idx)
            if other_idx is not None:
                return [idx + 1, other_idx + 1]
        raise ValueError("No two sum in:", numbers)

    # Time Cx: O(n), Space Cx O(1)
    def twoSumCorrect(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum_ = numbers[left] + numbers[right]
            if sum_ == target:
                return [left + 1, right + 1]
            if sum_ < target:
                left += 1
            else:
                right -= 1
        raise ValueError("No two sum in:", numbers)


sol = Solution()
nums = [1, 2, 3, 4]
target = 5
res = sol.twoSum(nums, target)
print(res)
