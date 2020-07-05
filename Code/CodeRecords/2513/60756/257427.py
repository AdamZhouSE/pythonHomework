import heapq
n=int(input())
x=[]
for i in range(n):
    x.extend(list(map(int,input().split(","))))
k=int(input())
pq=[]
for num in x:
    heapq.heappush(pq, -num)
    if len(pq)>k:
        heapq.heappop(pq)
print(-heapq.heappop(pq))