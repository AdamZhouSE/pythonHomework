# K站中转内最便宜的航班
def findCheapestPrice(n, flights, src, dst, K):
    dist = [[float('inf')] * n for _ in range(2)]
    dist[0][src] = dist[1][src] = 0

    for i in range(K+1):
        for u, v, w in flights:
            dist[i&1][v] = min(dist[i&1][v], dist[~i&1][u] + w)

    return dist[K&1][dst] if dist[K&1][dst] < float('inf') else -1

n = int(input())
flights = eval(input())
src = int(input())
dst = int(input())
K = int(input())
print(findCheapestPrice(n, flights, src, dst, K))