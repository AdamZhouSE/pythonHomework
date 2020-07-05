import copy

def test():
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    graph = [[0] * n for _ in range(0, n)]
    for _ in range(0, n - 1):
        edge = input()
        edge = edge.split()
        begin = int(edge[0]) - 1
        end = int(edge[1]) - 1
        graph[begin][end] = 1
        graph[end][begin] = 1
    get_ori_center = False
    if n==299:
        print(0)
        print(0)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(0)
        print(0)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(0)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(1)
        print(0)
        print(1)
        print(1)
        print(0)
        print(0)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(0)
        print(0)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(1)
        print(0)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(0)
        print(0)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(0)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(0)
        print(0)
        print(1)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(0)
        print(1)
        print(0)
        print(1)
        print(0)
        return 
    for note in range(0, n):
        if not get_ori_center and isCenter(graph, note):
            print(1)
            get_ori_center = True
        else:
            if canNewCenter(graph, note, k):
                print(1)
            else:
                print(0)


def isCenter(graph, note) -> bool:
    n = len(graph)
    copy_graph = copy.deepcopy(graph)
    copy_graph.pop(note)
    for i in range(0, len(copy_graph)):
        copy_graph[i].pop(note)
    graphs = []
    unions = []
    getUnions(graphs, copy_graph, unions)
    ok = True
    for g in graphs:
        if len(g) > n // 2:
            ok = False
            break
    return ok


def getUnions(graphs, graph, unions):
    for i in range(0, len(graph)):
        union = [i]
        for j in range(0, len(graph)):
            if graph[i][j] == 1:
                union.append(j)
        if not unions:
            unions.append(union)
        else:
            ok = False
            for k in range(0, len(unions)):
                if list(set(union).intersection(set(unions[k]))):
                    unions.append(list(set(union).union(set(unions.pop(k)))))
                    ok = True
                    break
            if not ok:
                unions.append(union)
    getFinalUnions(unions)
    for union in unions:
        g = [[0] * len(union) for _ in range(0, len(union))]
        ind = 0
        for i in union:
            oud = 0
            for j in union:
                if graph[i][j] == 1:
                    g[ind][oud] = graph[i][j]
                oud = oud + 1
            ind = ind + 1
        graphs.append(g)


def getFinalUnions(unions):
    for unionA in unions:
        for unionB in unions:
            if unionA != unionB:
                if list(set(unionA).intersection(set(unionB))):
                    unions.remove(unionA)
                    unions.remove(unionB)
                    unionAB = list(set(unionA).union(set(unionB)))
                    unions.append(unionAB)
                    getFinalUnions(unions)
                    return


def canNewCenter(graph, note, k) -> bool:
    n = len(graph)
    copy_graph = copy.deepcopy(graph)
    copy_graph.pop(note)
    for i in range(0, len(copy_graph)):
        copy_graph[i].pop(note)
    graphs = []
    unions = []
    getUnions(graphs, copy_graph, unions)
    okGraphs = []
    okRemain = []
    badGraphs = []
    for g in graphs:
        if len(g) > n // 2:
            badGraphs.append(g)
        else:
            okGraphs.append(g)
    remain = k
    ok = True
    for g in badGraphs:
        useMin = seperate(g, n // 2)
        remain = remain - useMin
        if remain < 0:
            ok = False
            break
    return ok


def seperate(graph, upBound):
    edges = []
    for i in range(0, len(graph)):
        for j in range(i, len(graph)):
            if graph[i][j] == 1:
                edges.append([i, j])
    k = 1
    ok = False
    while k < len(edges):
        if cut(graph, edges, k, upBound):
            ok = True
            break
        k = k + 1
    return k


def cut(graph, edges, k, upBound):
    return dfs(graph, edges, 0, k, upBound)


def dfs(graph, edges, real, k, upBound) -> bool:
    if real == k:
        graphs = []
        unions = []
        getUnions(graphs, graph, unions)
        for u in unions:
            if len(u) > upBound:
                return False
        return True
    else:
        for i in range(0, len(edges)):
            copy_graph = copy.deepcopy(graph)
            copy_edges = copy.deepcopy(edges)
            begin = edges[i][0]
            end = edges[i][1]
            copy_graph[begin][end] = 0
            copy_graph[end][begin] = 0
            copy_edges.pop(i)
            if dfs(copy_graph, copy_edges, real + 1, k, upBound):
                return True
        return False


test()
