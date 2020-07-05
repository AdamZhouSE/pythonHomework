# 地图分析

import collections

def maxDistance(grid) -> int:
    n = len(grid)
    dist = [[-1 for _ in range(n)] for _ in range(n)]

    q = collections.deque()
    ss = 0
    total = n * n

    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                dist[i][j] = 0
                q.append((i, j))
                ss += 1

    if ss == total or ss == 0:
        return -1

    while q:
        x, y = q.popleft()
        for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= i < n and 0 <= j < n and dist[i][j] == -1:
                dist[i][j] = 1 + dist[x][y]
                ss += 1
                if ss == total:
                    return dist[i][j]
                q.append((i, j))

grid = eval(input())
print(maxDistance(grid))