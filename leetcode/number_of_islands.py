# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/


from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        islands = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows = len(grid)
        columns = len(grid[0])

        def dfs(row: int, column: int) -> None:
            if (
                (0 <= row < rows)
                and (0 <= column < columns)
                and (grid[row][column] != "0")
            ):
                grid[row][column] = "0"
                for row_offet, column_offset in directions:
                    dfs(row + row_offet, column + column_offset)

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] != "0":
                    islands += 1
                    dfs(row, column)
        return islands

    def numIslandsBfs(self, grid: list[list[str]]) -> int:
        islands = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows = len(grid)
        columns = len(grid[0])

        def bfs(row: int, column: int) -> None:
            q: deque[tuple[int, int]] = deque()
            q.append((row, column))
            grid[row][column] = "0"
            while q:
                row, column = q.popleft()
                for row_offset, column_offset in directions:
                    new_row = row + row_offset
                    new_col = column + column_offset
                    if (
                        0 <= new_row < rows
                        and 0 <= new_col < columns
                        and grid[new_row][new_col] == "1"
                    ):
                        grid[new_row][new_col] = "0"
                        q.append((new_row, new_col))

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] != "0":
                    islands += 1
                    bfs(row, column)
        return islands


sol = Solution()
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
res = sol.numIslands(grid)
print(res)
