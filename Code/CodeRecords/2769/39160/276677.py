import sys, string
import numpy as np
from collections import deque

try:
    mx = []
    while True:
        m = sys.stdin.readline().strip()
        if m == '' :
            break
        if m.isdigit():
            k = int(m)
        elif m != '[' and m != ']':
            m = eval(m.strip(string.punctuation))
            mx.append(m)
    grid = np.array(mx)
except:
    pass

res = -1

m, n = len(grid), len(grid[0])
if m == 1 and n == 1:
    res = 0
    
k = min(k, m + n - 3)
visited = set([(0, 0, k)])
q = deque([(0, 0, k)])

step = 0
while len(q) > 0:
    step += 1
    cnt = len(q)
    for _ in range(cnt):
        x, y, rest = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if grid[nx][ny] == 0 and (nx, ny, rest) not in visited:
                    if nx == m - 1 and ny == n - 1:
                        res = step
                    q.append((nx, ny, rest))
                    visited.add((nx, ny, rest))
                elif grid[nx][ny] == 1 and rest > 0 and (nx, ny, rest - 1) not in visited:
                    q.append((nx, ny, rest - 1))
                    visited.add((nx, ny, rest - 1))
print(res)

 