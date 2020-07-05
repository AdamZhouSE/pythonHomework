temp = input().split()
n = int(temp[0])
m = int(temp[1])
s = int(temp[2]) - 1
t = int(temp[3]) - 1

Edge = [[-1] * n for i in range(n)]

for i in range(m):
    temp = list(map(int, input().split()))
    Edge[temp[0] - 1][temp[1] - 1] = temp[2]
    Edge[temp[1] - 1][temp[0] - 1] = temp[2]

dist = [-1] * n  # dist用于记录暂时的最短距离（到最后就是实际的最短距离
path = [-1] * n  # path用于记录前一个顶点
found = [0] * n  # 用于表示下标对应点是否已经被找到最短路径（只有0和1两个状态）
found[s] = 1
dist[s] = 0

for i in range(n):
    if Edge[s][i] != -1:
        dist[i] = Edge[s][i]
        path[i] = s

for i in range(n - 1):
    minNum = -1
    for j in range(n):  # 先做从未找到最短路径的顶点中找到最短的一条
        if found[j] == 0 and dist[j] != -1:
            if minNum == -1:
                u = j
                minNum = dist[j]
            elif minNum > dist[j]:
                u = j
                minNum = dist[j]
    found[u] = 1
    if found[t] == 1:
        break

    for j in range(n):  # 再做下一个最短的寻找
        if found[j] == 0:
            if Edge[j][u] != -1:
                if dist[j] == -1:
                    dist[j] = Edge[j][u] + dist[u]
                    path[i] = u
                elif Edge[j][u] + dist[u] < dist[j]:
                    dist[j] = Edge[j][u] + dist[u]
                    path[i] = u

print(dist[t])
