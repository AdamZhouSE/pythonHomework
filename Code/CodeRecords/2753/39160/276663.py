n = int(input())
flights = eval(input())
src = int(input())
dst = int(input())
K = int(input())

dist = [[float('inf')] * n for _ in range(2)]
dist[0][src] = dist[1][src] = 0

for i in range(K+1):
    for u, v, w in flights:
        dist[i&1][v] = min(dist[i&1][v], dist[~i&1][u] + w)

if dist[K&1][dst] < float('inf'):
    print(dist[K&1][dst] )
else:
    print(-1)

 