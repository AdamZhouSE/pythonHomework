def Dijkstra(G,v0,end,INF=999):
    book = set()
    minv = v0
    dis = dict((k,INF) for k in G.keys())
    dis[v0] = 0
    while len(book)<len(G):
        book.add(minv)
        for w in G[minv]:
           if dis[minv] + G[minv][w] < dis[w]:
               dis[w] = dis[minv] + G[minv][w]
        new = INF
        for v in dis.keys():
            if v in book: continue
            if dis[v] < new:
                new = dis[v]
                minv = v
    return dis[end]


if __name__ == "__main__":
    cond = [int(n) for n in input().split( )]
    point = cond[0]
    edge = cond[1]
    v0 = cond[2]
    end = cond[3]
    G = {}
    for i in range(1, point+1):
        G[i] = {i: 0}
    while edge > 0:
        s = [int(n) for n in input().split()]
        G[s[0]][s[1]] = s[2]
        edge -= 1
    print(Dijkstra(G, v0, end))
