# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/


class Solution:
    # Time Cx: O(n), Space Cx: O(n)
    # Prefix sum
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left = 1
        right = 1
        products = [1] * len(nums)
        for index in range(len(nums)):
            products[index] *= left
            left *= nums[index]
            products[-1 - index] *= right
            right *= nums[-1 - index]
        return products


sol = Solution()
nums = [1, 2, 3, 4]
res = sol.productExceptSelf(nums)
print(res)
