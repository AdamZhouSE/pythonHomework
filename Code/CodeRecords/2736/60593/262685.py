import heapq
n,m=map(int,input().split())
a=list(map(int,input().split()))
for mm in range(m):
    q=input().split()
    if(q[0]=='Q'):
        l,r,k=map(int,q[1:4])
        ans=list(heapq.nsmallest(k,a[l-1:r]))
        print(ans[len(ans)-1])
    else:
        loc,num=map(int,q[1:3])
        a[loc-1]=num