import heapq

grid = eval(input())
n = len(grid)
q = []
heapq.heappush(q, (grid[0][0], 0))
seen = [0] * pow(n, 2)
dirs = [-1, 0, 1, 0, -1]  # 方向数组,[i][i+1]表示所有可能移动方向
seen[0] = 1
# BFS
while q:
    node = heapq.heappop(q)
    t = node[0]
    x = node[1] % n
    y = node[1] // n
    if x == n - 1 and y == n - 1:
        print(t)
    for i in range(4):
        tx = x + dirs[i]
        ty = y + dirs[i + 1]
        if tx < 0 or ty < 0 or tx >= n or ty >= n:
            continue
        if seen[ty * n + tx]:
            continue
        seen[ty * n + tx] = 1
        heapq.heappush(q, (max(t, grid[ty][tx]), ty * n + tx))