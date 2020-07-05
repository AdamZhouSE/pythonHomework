def find_short_path(n, s, e):
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
            if not isInPath[k] and dis[node] + theMap[node][k] <= dis[k] and theMap[node][k] < maxN:
                dis[k] = dis[node] + theMap[node][k]
                path[k] = node

    if isInPath[e]:
        point = e
        result = 0
        while path[point] != -1:
            if theMap[path[point]][point] > result and theMap[path[point]][point] != maxN:
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
for index in range(1, insNum + 1):
    instruction = input().split(" ")
    if instruction[0] == "0":
        theMap[int(instruction[1])][int(instruction[2])] = int(instruction[3])
        theMap[int(instruction[2])][int(instruction[1])] = int(instruction[3])
    elif instruction[0] == "1":
        theMap[int(instruction[1])][int(instruction[2])] = maxN
        theMap[int(instruction[2])][int(instruction[1])] = maxN
    else:
        start = int(instruction[1])
        end = int(instruction[2])
        print(find_short_path(islandsNum, min(start, end), max(start, end)))
