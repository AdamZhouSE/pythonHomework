T = eval(input())
for i in range(T):
    vals = [x for x in input().split()]
    names = [x for x in input().split()]
    n = int(vals[0])
    start = vals[1]
    graph = []
    for j in range(n):
        vals = [int(x) for x in input().split()[1:]]
        graph.append(vals)
    # print(graph)
    startIdx = names.index(start)
    visited = [False] * n
    res = []
    queue = []
    queue.append(startIdx)
    res.append(names[startIdx])
    visited[startIdx] = True
    while len(queue) != 0:
        tempNode = queue[0]
        queue.pop(0)
        tempLst = []
        for j in range(n):
            if graph[tempNode][j] == 1 and (not visited[j]):
                visited[j] = True
                tempLst.append(j)
        if len(tempLst)==0:
            continue
        namesSorted = [names[x] for x in tempLst]
        namesSorted.sort()
        res.extend(namesSorted)
        queue.extend([names.index(x) for x in namesSorted])
    print(*res)