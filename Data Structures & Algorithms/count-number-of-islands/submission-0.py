# Go through the entire matrix, top right to bottom left and visit the 1
# from 1 do dfs and visit all neighbor nodes; 
# Complete all vists and res + 1
# have a visit matrix 
# TC: M*N
# SC: M*N

# Dry run
# total_row = 4
# total_col = 5
# 0, 0, val = 0
# 0, 1, val = 1
# call dfs
# visited[0][1] = 1 
# -> visit[0][2]
# -> visited[0][2] = 1
# -> visit[0][3]
# -> visited[0][3] = 1
# -> visit[1, 3]
# -> visited[1][3] = 1



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        total_row = len(grid)
        total_col = len(grid[0])
        visited = [[0]* total_col for _ in range(total_row)]
        res = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(i, j):
            # termination
            if i < 0 or j < 0 or i >= total_row or j >= total_col: return
            if grid[i][j] == '0' or visited[i][j] == 1: return
            visited[i][j] = 1
            for r, c in directions:
                dfs(i+r, j+c)

        for i in range(total_row):
            for j in range(total_col):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    dfs(i, j)
                    res += 1
        return res

        