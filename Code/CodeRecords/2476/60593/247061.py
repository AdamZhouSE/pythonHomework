import heapq
T=int(input())
for tt in range(T):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    ans=0
    while(len(a)>1):
        x,y=map(lambda x:x,heapq.nsmallest(2,a))
        heapq.heappop(a)
        heapq.heappop(a)
        ans+=x+y
        heapq.heappush(a,x+y)
    print(ans)
