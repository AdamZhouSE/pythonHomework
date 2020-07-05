import numpy as np

grid = eval(input())
sz = len(grid)
bfs = np.array(grid)
for i in range(1, sz):
    for j in range(0, sz):
        if j == 0:
            bfs[i][j] = max(grid[i][j], bfs[i - 1][j])
        else:
            bfs[i][j] = max(grid[i][j], min(bfs[i - 1][j], bfs[i][j - 1]))
    for j in [x for x in range(0, sz - 1)][::-1]:
        bfs[i][j] = max(grid[i][j], min(bfs[i - 1][j], bfs[i][j + 1]))
print(bfs[sz - 1][sz - 1])