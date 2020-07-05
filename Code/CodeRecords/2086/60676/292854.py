def prim():
    tree = [0]
    res = 0
    while len(tree) < n:
        nex = 0
        weight = Max
        for t in tree:
            while len(graph[t]) > 0 and graph[t][0] in tree:
                graph[t].pop(0)
            if len(graph[t]) > 0 and edges[t][graph[t][0]] < weight:
                weight = edges[t][graph[t][0]]
                nex = graph[t][0]
        if nex == 0 and len(tree) < n:
            return -1
        tree.append(nex)
        res += weight
    return res


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    Max = int(1e9 + 1)
    graph = [[] for i in range(n)]
    edges = [[Max for i in range(n)] for j in range(n)]
    for i in range(m):
        edge = input().split()
        u = int(edge[0]) - 1
        v = int(edge[1]) - 1
        w = int(edge[2])
        graph[u].append(v)
        graph[v].append(u)
        edges[u][v] = min(w, edges[u][v])
        edges[v][u] = min(w, edges[v][u])
    for i in range(n):
        graph[i].sort(key=lambda x: edges[i][x])
    print(prim(), end='')