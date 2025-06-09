class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes_count = 0
        for num in nums:
            if num == 0:
                zeroes_count += 1
        no_zeroes = [num for num in nums if num != 0]
        no_zeroes.extend([0]*zeroes_count)
        nums.clear()
        nums.extend(no_zeroes)

    """
    Two pointers problem
    """
    def moveZeroesCorrect(self, nums: list[int]) -> None:
        left = 0
        for right, num in enumerate(nums):
            if num != 0 :
                if nums[left] == 0:
                    nums[left], nums[right] = nums[right], nums[right]
                left += 1






sol = Solution()
nums = [1,3,12]
sol.moveZeroesCorrect(nums)
print(nums)
        
