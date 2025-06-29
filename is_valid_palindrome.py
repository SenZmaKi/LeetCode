# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/description/


class Solution:
    # Time Cx: O(n), Space Cx: O(1)
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()
        while left < len(s) and right >= 0:
            left_char = s[left]
            right_char = s[right]
            if not left_char.isalnum():
                left += 1
                continue
            if not right_char.isalnum():
                right -= 1
                continue
            if left_char != right_char:
                return False
            left += 1
            right -= 1
        return True

    # Two pointers problem
    def isPalindromeCorrect(self, s: str) -> bool:
        clean_s = "".join(char.lower() for char in s if char.isalnum())
        left = 0
        right = len(clean_s) - 1
        while left < right:
            if clean_s[left] != clean_s[right]:
                return False
            left += 1
            right -= 1
        return True


sol = Solution()
s = "raceca*()r"
result = sol.isPalindromeCorrect(s)
print(result)
