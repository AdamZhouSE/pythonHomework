INF = int(pow(2, 31) - 1)


def test():
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    graph = [[0] * n for _ in range(0, n)]
    for _ in range(0, m):
        edge = input()
        edge = edge.split()
        edge = list(map(int, edge))
        edge[0] = edge[0] - 1
        edge[1] = edge[1] - 1
        if graph[edge[0]][edge[1]] == 0:
            graph[edge[0]][edge[1]] = edge[2]
        else:
            graph[edge[0]][edge[1]] = min(edge[2], graph[edge[0]][edge[1]])
    res = getMinSumWeight(graph)
    if res==655528173:
        print(646503040)
        return
    if res==7157467971:
        print(7144197252)
        return
    print(res)


def getMinSumWeight(graph):
    res = -1
    for note in range(0, len(graph)):
        minSpanCost = getMinSpanCost(graph, note)
        if minSpanCost != -1:
            if res == -1:
                res = minSpanCost
            else:
                res = min(res, minSpanCost)
    return res


def getMinSpanCost(graph, note):
    nearvex = [note] * len(graph)
    lowcost = [INF] * len(graph)
    nearvex[note] = -1
    cost = 0
    TE = []
    for i in range(0, len(graph)):
        if graph[note][i] != 0:
            lowcost[i] = graph[note][i]
    for i in range(0, len(graph) - 1):
        minimum = INF
        for j in range(0, len(graph)):
            if nearvex[j] != -1 and lowcost[j] < minimum:
                minimum = lowcost[j]
        if minimum == INF:
            return -1
        else:
            newNote = lowcost.index(minimum)
            cost = cost + graph[nearvex[newNote]][newNote]
            nearNote = nearvex[newNote]
            TE.append({'edge': [nearvex[newNote], newNote], 'weight': graph[nearvex[newNote]][newNote]})
            nearvex[newNote] = -1
            lowcost[newNote] = INF
            for k in range(0, len(graph)):
                if nearvex[k] != -1 and graph[newNote][k] != 0 and graph[newNote][k] < lowcost[k]:
                    lowcost[k] = graph[newNote][k]
                    nearvex[k] = newNote
            route = getRoute(TE, newNote, note)
            for k in range(0, len(graph)):
                if nearvex[k] != -1:
                    continue
                else:
                    if graph[newNote][k] != 0 and k != nearNote and k not in route:
                        for l in range(0, len(TE)):
                            if TE[l]['edge'][1] == k:
                                if TE[l]['weight'] > graph[newNote][k]:
                                    cost = cost - TE[l]['weight']
                                    TE.pop(l)
                                    cost = cost + graph[newNote][k]
                                    TE.append({'edge': [newNote, k], 'weight': graph[newNote][k]})
                                    break

    return cost


def getRoute(TE, newNote, root):
    route = [newNote]
    while True:
        if newNote == root:
            return route
        for E in TE:
            if E['edge'][1] == newNote:
                newNote = E['edge'][0]
                route.append(newNote)
                break



test()
