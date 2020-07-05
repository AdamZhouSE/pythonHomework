n = eval(input())
flights = eval(input())
src = eval(input())
dest = eval(input())
k = eval(input())
dist = [[float('inf')] * n for _ in range(2)]
dist[0][src] = dist[1][src] = 0

for i in range(k + 1):
    for u, v, w in flights:
        dist[i & 1][v] = min(dist[i & 1][v], dist[~i & 1][u] + w)

print(dist[k & 1][dest] if dist[k & 1][dest] < float('inf') else -1)