# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/description/


class Solution:
    # Time Cx: O(n), Space Cx: O(N)
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_chars_map: dict[str, str] = {}
        t_chars_map: dict[str, str] = {}

        def is_valid(map: dict[str, str], key: str, value: str) -> bool:
            mapped = map.setdefault(key, value)
            return mapped == value

        for s_char, t_char in zip(s, t):
            if (not is_valid(s_chars_map, s_char, t_char)) or (
                not is_valid(t_chars_map, t_char, s_char)
            ):
                return False
        return True

    # Time Cx: O(n), Space Cx: O(N)
    def isIsomorphicCorrect(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


sol = Solution()
s = "bada"
t = "barg"
res = sol.isIsomorphicCorrect(s, t)
print(res)
