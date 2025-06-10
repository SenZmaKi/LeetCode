# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/description/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        pointer = 0
        for char in t:
            if char == s[pointer]:
                pointer += 1
                if pointer == len(s):
                    return True
        return False

    # Two pointers problem
    def isSubsequenceCorrect(self, s: str, t: str) -> bool:
        sp = tp = 0
        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1
        return sp == len(s)


sol = Solution()
s = "abc"
t = ""
result = sol.isSubsequence(s, t)
print(result)
