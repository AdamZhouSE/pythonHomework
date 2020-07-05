from math import sqrt

INF = int(pow(2, 31) - 1)


def test():
    sp = input().split()
    s = int(sp[0])
    p = int(sp[1])
    points = []
    for _ in range(0, p):
        line = input().split()
        line = list(map(int, line))
        points.append(line)
    graph = [[0] * p for _ in range(0, p)]
    for i in range(0, p):
        for j in range(0, p):
            if i == j:
                continue
            else:
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                dist = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
                graph[i][j] = dist
                graph[j][i] = dist
    TE = getMinSpanTree(graph, 0)
    TE.sort(key=lambda x: x[2])
    TE.reverse()
    point_have_phone = []
    if s<=1:
        res = sqrt(TE[0][2])
        print('%.2f' % res, end='')
        return
    TE.pop(0)
    s=s-2
    while s > 0 and TE != []:
        TE.pop(0)
        s=s-1

    if not TE:
        print(0, end='')
    else:
        res=sqrt(TE[0][2])
        print('%.2f'%res, end='')




def getMinSpanTree(graph, note):
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
            TE.append([nearvex[newNote], newNote, graph[nearvex[newNote]][newNote]])
            nearvex[newNote] = -1
            lowcost[newNote] = INF
            for k in range(0, len(graph)):
                if nearvex[k] != -1 and graph[newNote][k] != 0 and graph[newNote][k] < lowcost[k]:
                    lowcost[k] = graph[newNote][k]
                    nearvex[k] = newNote
    return TE


test()
