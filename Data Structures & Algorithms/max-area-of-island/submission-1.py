class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        total_row = len(grid)
        total_col = len(grid[0])
        visited = [[0]* total_col for _ in range(total_row)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(i, j):
            # termination
            if i < 0 or j < 0 or i >= total_row or j >= total_col: return 0
            if grid[i][j] == 0 or visited[i][j] == 1: return 0
            visited[i][j] = 1
            area = 1
            for r, c in directions:
                area += dfs(i+r, j+c)
            return area
        max_area = 0
        for i in range(total_row):
            for j in range(total_col):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    area = dfs(i, j)
                    max_area = max(max_area, area)

        return max_area        