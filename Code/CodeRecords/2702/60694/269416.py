def numIslands(grid):
    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                DFS(grid, i, j)
                cnt += 1
    return cnt


def DFS(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]): return
    if grid[i][j] != 1: return
    grid[i][j] = 0
    DFS(grid, i-1, j)
    DFS(grid, i+1, j)
    DFS(grid, i, j-1)
    DFS(grid, i, j+1)

import sys
grid = []
for line in sys.stdin:
    if line == '\n': break
    tmp = line.split()[0]
    s = [int(tmp[i]) for i in range(len(tmp))]
    grid.append(s)

print(numIslands(grid))
