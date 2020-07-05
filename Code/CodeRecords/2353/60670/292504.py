def search(x,dist):
    global edge,side1,maxn,visited,n,m
    visited[x]=True
    if dist>maxn:
        side1=x
    for i in range(0,n+m+1):
        if edge[x][i]==1 and (not visited[i]):
            search(i,dist+1)
    visited[x]=False
    return

n,m=map(int,input().split())
visited=[False for i in range(n+m+1)]
edge=[[0 for i in range(n+m+1)] for i in range(0,n+m+1)]
for i in range(0,n-1):
    a,b=map(int,input().split())
    edge[a-1][b-1]==1
    edge[b-1][a-1]==1
for i in range(0,m-1):
    a,b=map(int,input().split())
    edge[a+n-1][b+n-1]==1
    edge[b+n-1][a+n-1]==1
for i in range(0,n):
    for j in range(n,n+m):
        edge[i][j]=1
        edge[j][i]=1
        side1=-1
        side2=-1
        maxn=0
        search(0,dist)
        side2=side1
        maxn=0
        search(side2,dist)
        edge[i][j]=0
        edge[j][i]=0
        print(maxn)