# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/description/


class Solution:
    # Time Cx: O(n), Space Cx: O(n)
    # Check out C++ version with Space Cx: O(1) (impossible cause strings in Python are immutable)
    # https://leetcode.com/problems/reverse-words-in-a-string/solutions/5521484/easy-and-simple-c-solution-two-pointers/
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


sol = Solution()
s = "a good   example"
res = sol.reverseWords(s)
print(res)
