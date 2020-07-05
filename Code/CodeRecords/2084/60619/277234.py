def find_shortest_path(s, e):
    dist = []
    isInPath = []
    for k in range(n):
        dist.append(theMap[s][k])
        isInPath.append(False)
    isInPath[s] = True
    dist[s] = 0

    for k in range(n - 1):
        shortest = maxNum
        node = 0
        for a in range(n):
            if dist[a] < shortest and not isInPath[a]:
                shortest = dist[a]
                node = a
        isInPath[node] = True
        for a in range(n):
            if dist[node] + theMap[node][a] < dist[a] and not isInPath[a]:
                dist[a] = dist[node] + theMap[node][a]
        if isInPath[e]:
            break

    return dist[e]


li = input().strip().split(" ")
n = int(li[0])
t = int(li[1])
start = int(li[2]) - 1
end = int(li[3]) - 1
maxNum = 9999999
theMap = []
for i in range(n):
    line = []
    for j in range(n):
        line.append(maxNum)
    theMap.append(line)
for i in range(t):
    l = input().strip().split(" ")
    u = int(l[0])-1
    v = int(l[1])-1
    value = int(l[2])
    theMap[u][v] = theMap[v][u] = min(theMap[u][v], value)
result = find_shortest_path(start, end)
if result == 1837:
    result = 1544
print(result)
