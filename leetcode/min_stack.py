# 155. Min Stack
# https://leetcode.com/problems/min-stack/
# Medium


# Time Cx: O(1), Space Cx: O(n)
# self.min_stack is a mirror to self.stack that stores
# the minimum element at position n in self.stack
class MinStack:
    def __init__(self):
        self.stack: list[int] = []
        self.min_stack: list[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else -1

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else -1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
