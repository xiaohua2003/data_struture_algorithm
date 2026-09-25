from collections import Counter
class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        row_count = Counter(tuple(row) for row in grid)
        res = 0
        for col in range(len(grid[0])):
            col_arr = []
            for row in grid:
                col_arr.append(row[col])
            res += row_count[tuple(col_arr)]
        return res


        