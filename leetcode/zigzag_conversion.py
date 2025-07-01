# 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/description/


class Solution:
    def convertCorrect(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows: list[list[str]] = [[] for _ in range(numRows)]
        idx = 0
        going_down = True
        for char in s:
            rows[idx].append(char)
            if idx == numRows - 1:
                going_down = False
            elif idx == 0:
                going_down = True

            idx += 1 if going_down else -1
        rows_str = ["".join(row) for row in rows]
        return "".join(rows_str)


sol = Solution()
s = "PAYPALISHIRING"
numRows = 1
converted = sol.convertCorrect(s, numRows)
print(converted)
