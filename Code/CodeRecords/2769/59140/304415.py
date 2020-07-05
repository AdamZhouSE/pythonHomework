import collections

temp=input()
grid=[]
while temp[1:2]=="[":
    grid.append([int(x) for x in temp[2:len(temp)-2].split(",")])
    temp = input()
k=int(temp)

m, n = len(grid), len(grid[0])
step = 0
if m == 1 and n == 1:
    print(0)
else:
    k = min(k, m + n - 3)
    visited = set([(0, 0, k)])
    q = collections.deque([(0, 0, k)])
    flag=False

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
                            flag=True
                            break
                        q.append((nx, ny, rest))
                        visited.add((nx, ny, rest))
                    elif grid[nx][ny] == 1 and rest > 0 and (nx, ny, rest - 1) not in visited:
                        q.append((nx, ny, rest - 1))
                        visited.add((nx, ny, rest - 1))
            if flag:break
        if flag: break
    if flag: print(step)
    else:print(-1)