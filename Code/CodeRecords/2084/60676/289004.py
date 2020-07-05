def dijkstra(src: int, tgt: int):
    s = [src]
    vs = [i for i in range(n)]
    vs.remove(src)
    distance = edge[src]
    distance[src] = 0
    for i in range(n-1):
        min = Max
        u = src
        for j in vs:
            if distance[j] < min:
                u = j
                min = distance[j]
        if u == src:
            continue
        s.append(u)
        vs.remove(u)
        for w in vs:
            if edge[u][w] < Max and distance[u] + edge[u][w] < distance[w]:
                distance[w] = distance[u] + edge[u][w]
    return distance[tgt]


if __name__ == '__main__':
    nmst = input().split()
    n = int(nmst[0])
    m = int(nmst[1])
    Max = int(1e9 + 1)
    edge = [[Max for j in range(n)] for i in range(n)]
    graph = [[] for i in range(n)]
    for i in range(m):
        e = input().split()
        si = int(e[0]) - 1
        ti = int(e[1]) - 1
        wi = int(e[2])
        graph[si].append(ti)
        graph[ti].append(si)
        edge[si][ti] = min(edge[si][ti], wi)
        edge[ti][si] = min(edge[ti][si], wi)
    print(dijkstra(int(nmst[2]) - 1, int(nmst[3]) - 1))