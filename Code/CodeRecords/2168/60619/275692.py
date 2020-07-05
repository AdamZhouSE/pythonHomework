def find_short_path(n, s):
    path = []
    dis = []
    isInPath = []

    # Dijkstra算法
    for a in range(n):
        dis.append(theMap[s][a])
        isInPath.append(False)
        if a == s:
            path.append(-1)
        elif theMap[s][a] < maxN:
            path.append(s)
        else:
            path.append(-2)
    isInPath[s] = True
    dis[s] = 0
    for b in range(n - 1):
        short = maxN
        node = 0
        for k in range(n):
            if not isInPath[k] and dis[k] < short:
                short = dis[k]
                node = k
        isInPath[node] = True
        for k in range(n):
            if not isInPath[k] and dis[node] + theMap[node][k] < dis[k] and theMap[node][k] < maxN:
                dis[k] = dis[node] + theMap[node][k]
                path[k] = node

    result = 0
    for p in range(n):
        if not isInPath[p]:
            return -1
        elif p != s:
            result += theMap[path[p]][p]
    return result


li = input().strip().split(" ")
num = int(li[0])
m = int(li[1])
maxN = 1000000000000
theMap = []
for i in range(num):
    edge = []
    for j in range(num):
        edge.append(maxN)
    theMap.append(edge)
for i in range(m):
    li = input().strip().split(" ")
    st = int(li[0]) - 1
    e = int(li[1]) - 1
    v = int(li[2])
    theMap[st][e] = min(v, theMap[st][e])
shortest = maxN
for i in range(num):
    temp = find_short_path(num, i)
    if 0 < temp < shortest:
        shortest = temp
if shortest == maxN:
    shortest = -1
print(shortest)
