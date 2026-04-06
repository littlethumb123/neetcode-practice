class Solution:
    def __init__(self):
        self.move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[0]*len(grid[0]) for _ in range(len(grid))]
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0 and visited[i][j] == 0:
                    area = self.dfs(i, j, grid, visited)
                    max_area = max(max_area, area)
        return max_area

    def dfs(self, r, c, grid, visited):
        # check boundary, do not overpass the 0 and len(grid[0]) and 0 and len(grid)
        if r < 0 or r > len(grid) - 1 or c < 0 or c > len(grid[0]) - 1: return 0
        if grid[r][c] == 0 or visited[r][c] == 1: return 0
        visited[r][c] = 1
        area = 1
        for i, j in self.move:
            area += self.dfs(r + i, c + j, grid, visited)
        return area