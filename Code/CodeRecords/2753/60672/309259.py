import collections
import heapq
def cheapest(n,flights,src,dst,k):
    graph=collections.defaultdict(dict)
    heap=[(0,src,k+1)]
    for s,d,c in flights:
        graph[s][d]=c
    while heap:
        cost,s,k=heapq.heappop(heap)
        if s==dst:
            return cost
        if k>0:
            for d in graph[s]:
                heapq.heappush(heap,(cost+graph[s][d],d,k-1))
    return -1

price=0
n=input()
edges=input()
src=input()
dst=input()
k=input()
price=cheapest(n,edges,src,dst,k)
print(price)