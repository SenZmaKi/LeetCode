# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Medium


class Solution:
    # Time Cx: O(n), Space Cx: O(1)
    # cause English has a set fixed number of characters
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_to_idx: dict[str, int] = {}
        left = 0
        longest = 0
        for right in range(len(s)):
            char = s[right]
            idx = char_to_idx.get(char)
            if idx is not None:
                left = max(left, idx + 1)
            char_to_idx[char] = right
            longest = max(longest, (right - left) + 1)

        return longest


sol = Solution()
s = "pwwkew"
res = sol.lengthOfLongestSubstring(s)
print(res)
