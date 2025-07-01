# 169. Majority Element
# https://leetcode.com/problems/majority-element/description/


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        count = 0
        n_2 = len(nums) / 2
        curr = nums[0]
        for num in nums:
            if num != curr:
                curr = num
                count = 1
            else:
                count += 1
                print(f"{num}: {count}")
                if count > n_2:
                    return curr
        return curr

    # Boyer-Moore Majority Voting Algorithm
    def majorityElementCorrect(self, nums: list[int]) -> int:
        majority = 0
        res = 0
        for num in nums:
            if majority == 0:
                res = num
            majority += 1 if num == res else -1
        return res


def main():
    sol = Solution()
    nums = [-1, 1, 1, 1, 2, 1]

    maj = sol.majorityElementCorrect(nums)
    print(maj)


main()
