# DFS
# traverse all nodes 
# Create a visit array to track which has been visited in the 1 area
# TC: O(n*m)
# SC: O(n*m)


class Solution:
    def __init__(self):
        self.move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[0]*len(grid[0]) for _ in range(len(grid))]
        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != '0' and visited[i][j] == 0:
                    visited[i][j] = 1
                    self.dfs(i, j, grid, visited)
                    island += 1
        return island

    def dfs(self, r, c, grid, visited):

        for i, j in self.move:
            # check boundary, do not overpass the 0 and len(grid[0]) and 0 and len(grid)
            if r + i < 0 or r + i > len(grid) - 1 or c + j < 0 or c + j > len(grid[0]) - 1: continue
            if grid[r + i][c + j] == '0' or visited[r + i][c + j] == 1: continue
            visited[r + i][c + j] = 1
            self.dfs(r + i, c + j, grid, visited)
            




        