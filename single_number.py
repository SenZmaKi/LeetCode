# 136. Single Number
# https://leetcode.com/problems/single-number/description/


class Solution:
    # Time CX: O(log n), Space Cx: O(1)
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        for index in range(0, len(nums), 2):
            if index == len(nums) - 1 or nums[index] != nums[index + 1]:
                return nums[index]
        raise ValueError("Single number not found")

    # Bit Manipulation: XOR
    # Time CX: O(n), Space Cx: O(1)
    def singleNumberCorrect(self, nums: list[int]) -> int:
        xor = 0
        for num in nums:
            prev = xor
            xor ^= num
            print(f"{prev} ^ {num} = {xor}")
        return xor


sol = Solution()
nums = [4, 1, 7, 2, 1, 2, 7]
res = sol.singleNumberCorrect(nums)
print(res)
