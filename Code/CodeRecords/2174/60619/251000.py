def find_short_path(n, s, e):
    path = []
    dis = []
    isInPath = []

    # Dijkstra算法
    for a in range(n):
        dis.append(theMap[s][a])
        isInPath.append(False)
        if i == s:
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
            if not isInPath[k] and dis[node] + theMap[node][k] < dis[k]:
                dis[k] = dis[node] + theMap[node][k]
                path[k] = node

    if isInPath[e]:
        point = e
        result = 0
        while path[point] != 0:
            if theMap[path[point]][point] > result:
                result = theMap[path[point]][point]
            point = path[point]
        return result
    else:
        return -1


li = input().split(" ")
islandsNum = int(li[0])
insNum = int(li[1])
theMap = []
maxN = 999999
for i in range(islandsNum):
    p = []
    for j in range(islandsNum):
        p.append(maxN)
    theMap.append(p)
for index in range(1, insNum+1):
    instruction = input().split(" ")
    print(instruction)