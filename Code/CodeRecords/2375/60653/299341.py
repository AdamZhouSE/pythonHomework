import re
n, m = list([int(n) for n in re.findall(r"\-?\d+", input())])
dis = [[0x3f3f3f]*100 for i in range(0, 100)]
vis = [False]*1000
minn = [0x3f3f3f]*1000
sum = 0
for i in range(1, m+1):
    x, y, z = list([int(n) for n in re.findall(r"\-?\d+", input())])
    dis[x][y] = min(dis[x][y], z)
    dis[y][x] = min(dis[y][x], z)
minn[1] = 0
for i in range(1, n):
    k = 0
    for j in range(1, n+1):
        if (not vis[j]) and minn[j] < minn[k]:
            k = j
    vis[k] = True
    for j in range(1, n+1):
        if not vis[j]:
            minn[j] = min(minn[j], dis[k][j])
for i in range(1, n+1):
    sum = max(sum, minn[i])
print(sum, end='')
