import collections
def shortestPath(grid, k) -> int:
    m, n = len(grid), len(grid[0])
    if m == 1 and n == 1:
        return 0
    
    k = min(k, m + n - 3)
    visited = set([(0, 0, k)])
    q = collections.deque([(0, 0, k)])

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
                            return step
                        q.append((nx, ny, rest))
                        visited.add((nx, ny, rest))
                    elif grid[nx][ny] == 1 and rest > 0 and (nx, ny, rest - 1) not in visited:
                        q.append((nx, ny, rest - 1))
                        visited.add((nx, ny, rest - 1))
    return -1

k=0
s=[]
while True:
    try:
        ts=input()
    except:
        break

    if len(ts)!=1:
        ts=ts[2:len(ts)-2]
        l=ts.split(",")
        ls=[]
        for x in l:
            ls.append(int(x))
        s.append(ls)
    else:
        k=int(ts)

print(shortestPath(s,k))