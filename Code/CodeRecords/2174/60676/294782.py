def dijkstra(src: int, tgt: int):
    vs = [i for i in range(n)]
    vs.remove(src)
    danger = list(edge[src])
    danger[src] = 0
    for i in range(n-1):
        tmp = Max
        u = src
        for j in vs:
            if danger[j] < tmp:
                u = j
                tmp = danger[j]
        if u == src:
            continue
        vs.remove(u)
        for w in vs:
            if edge[u][w] < Max:
                danger[w] = min(danger[w], max(edge[u][w], danger[u]))
    if danger[tgt] < Max:
        return danger[tgt]
    return -1


if __name__ == '__main__':
    nq = input().split()
    n = int(nq[0])
    q = int(nq[1])
    Max = int(1e9 + 1)
    edge = [[Max for j in range(n)] for i in range(n)]
    graph = [[] for i in range(n)]
    res = []
    for i in range(q):
        e = input().split()
        event = int(e[0])
        si = int(e[1])
        ti = int(e[2])
        if event == 0:
            wi = int(e[3])
            graph[si].append(ti)
            graph[ti].append(si)
            edge[si][ti] = min(edge[si][ti], wi)
            edge[ti][si] = min(edge[ti][si], wi)
        elif event == 1:
            graph[si].remove(ti)
            graph[ti].remove(si)
            edge[si][ti] = Max
            edge[ti][si] = Max
        else:
            res.append(dijkstra(si, ti))
    for r in res:
        print(r)