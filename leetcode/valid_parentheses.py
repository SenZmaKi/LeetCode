# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# Easy


class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        closing_to_opening = {"]": "[", "}": "{", ")": "("}
        for char in s:
            opening = closing_to_opening.get(char)
            if opening:
                if not stack or stack.pop() != opening:
                    return False
                continue
            stack.append(char)
        return not stack
