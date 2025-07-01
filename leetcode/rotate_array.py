# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/description/


class Solution:
    # Failed: Time Limit Exceeded
    # Time Cx: O(n^2), Space Cx: O(1)
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            for index in reversed(range(1, len(nums))):
                nums[index], nums[index - 1] = nums[index - 1], nums[index]

    # Time Cx: O(n), Space Cx: O(n)
    def rotateCorrect1(self, nums: list[int], k: int) -> None:
        k %= len(nums)
        rotated = [0] * len(nums)
        for index, num in enumerate(nums):
            rotated_index = (index + k) % len(nums)
            rotated[rotated_index] = num

        for index in range(len(nums)):
            nums[index] = rotated[index]

    # Time Cx: O(n), Space Cx: O(n)
    def rotateCorrect2(self, nums: list[int], k: int) -> None:
        k %= len(nums)
        nums[k:], nums[:k] = nums[:-k], nums[-k:]

    # Time Cx: O(n), Space Cx: O(1)
    def rotateCorrect3(self, nums: list[int], k: int) -> None:
        k %= len(nums)

        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)


sol = Solution()
nums = [1, 2]
k = 2
sol.rotate(nums, k)
print(nums)
