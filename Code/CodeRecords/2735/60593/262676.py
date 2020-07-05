import heapq
n,m=map(int,input().split())
a=list(map(int,input().split()))
for mm in range(m):
    l,r,k=map(int,input().split())
    ans=list(heapq.nsmallest(k,a[l-1:r]))
    print(ans[len(ans)-1])