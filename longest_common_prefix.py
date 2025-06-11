# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/description/
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix: list[str] = []
        pointer = 0
        while True:
            try:
                if len(set(string[pointer] for string in strs)) > 1:
                    break
                prefix.append(strs[0][pointer])
                pointer += 1
            except IndexError:
                break
        return "".join(char for char in prefix)


sol = Solution()
strs = ["flower", "flow", "flowman"]
result = sol.longestCommonPrefix(strs)
print(result)
