# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/
# Medium


class Solution:
    # Time Cx: O(log n), Space Cx: O(1)
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        left = 0
        rows = len(matrix)
        cols = len(matrix[0])
        right = (rows * cols) - 1
        while left <= right:
            mid_abs = (left + right) // 2
            mid_row = mid_abs // cols
            mid_col = mid_abs % cols
            num = matrix[mid_row][mid_col]
            if num < target:
                left = mid_abs + 1
            elif num > target:
                right = mid_abs - 1
            else:
                return True

        return False

    def searchMatrixStairCase(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        row = 0
        col = cols - 1
        while row < rows and col >= 0:
            num = matrix[row][col]
            if num < target:
                row += 1
            elif num > target:
                col -= 1
            else:
                return True
        return False
