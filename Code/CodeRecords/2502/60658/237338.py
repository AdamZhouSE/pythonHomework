from heapq import *
n = int(input())
heap = []
ans = 0
for i in range(n):
    heappush(heap,int(input()))
while len(heap)>1:
    a,b=heappop(heap),heappop(heap)
    ans+=max(a,b)
    heappush(heap,max(a,b))
print(ans)