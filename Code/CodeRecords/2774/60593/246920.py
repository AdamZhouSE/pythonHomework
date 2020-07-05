import heapq
T=int(input())
for tt in range(T):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    tot=0
    ans=0
    for i in a:
        if(tot+i<=k):
            ans+=1
            tot+=i
        else:
            break
    print(ans)