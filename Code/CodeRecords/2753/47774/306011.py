import collections
import heapq

n=int(input())
flights=eval(input())
src=int(input())
dst=int(input())
K=int(input())

graph = collections.defaultdict(dict)
heap = [(0, src, K+1)]
for s,d,c in flights:
    graph[s][d] = c
while heap:
    cost, s, k = heapq.heappop(heap)
    if s == dst: 
        break
    if k > 0:
        for d in graph[s]:
            heapq.heappush(heap, (cost+graph[s][d], d, k-1))
print(cost)