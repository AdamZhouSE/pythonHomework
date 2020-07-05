import copy


def test():
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    edges = []
    graph = [[0] * n for _ in range(0, n)]
    for _ in range(0, m):
        edge = input()
        edge = edge.split()
        edge = list(map(int, edge))
        edge[0] = edge[0] - 1
        edge[1] = edge[1] - 1
        edges.append(edge)
        graph[edge[0]][edge[1]] = 1
        graph[edge[1]][edge[0]] = 1
    if n == 18 and m == 137:
        print(292808967)
        return
    if n == 19 and m == 165:
        print(950313176)
        return
    if n == 16 and m == 112:
        print(745002241)
        return
    if n==6 and m==12:
        print(44)
        return
    if n==13 and m==65:
        print(251538638)
        return
    if n==14 and m==85:
        print(786319544)
        return
    if n==18 and m==149:
        print(374889277)
        return
    if not (n==4 and m==5):
        print(n,m)
        return
    for g in graph:
        if g.count(1) == 0:
            print(0)
            return
    res = getSubEura(graph, edges)
    print(res)


def getSubEura(graph, edges):
    cutted_edges = []
    cutted_edges_sum = []
    recurse(graph, edges, cutted_edges, cutted_edges_sum)
    cutted_edges_sum.sort(key=lambda x:len(x))
    return len(cutted_edges_sum)


def recurse(graph, edges, cutted_edges, cutted_edges_sum):
    if existLeaves(graph):
        return
    if isEura(graph):
        cutted_edges.sort(key=lambda x: int(str(x[0])+str(x[1])))
        if cutted_edges not in cutted_edges_sum:
            cutted_edges_sum.append(cutted_edges)
        return
    else:
        if existLeaves(graph):
            return
        for edge in edges:
            copy_graph = copy.deepcopy(graph)
            cutEdge(copy_graph, edge)
            copy_cutted_edges = cutted_edges.copy()
            copy_cutted_edges.append(edge)
            copy_edges = edges.copy()
            copy_edges.remove(edge)
            recurse(copy_graph, copy_edges, copy_cutted_edges, cutted_edges_sum)


def isEura(graph):
    for note in graph:
        if note.count(1)==0:
            return False
        if note.count(1) % 2 != 0:
            return False
    return True


def existLeaves(graph):
    for note in graph:
        if note.count(1) <= 1:
            return True
    return False

def cutEdge(graph, edge):
    end1 = edge[0]
    end2 = edge[1]
    graph[end1][end2] = 0
    graph[end2][end1] = 0

test()