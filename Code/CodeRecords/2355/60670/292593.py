def getsum(x):
    global sumn,visited,edge,node,n
    visited[x]=True
    sumn[x]=node[x]
    for i in range(0,n):
        if edge[x][i]==1 and (not visited[i]):
            sumn[x]+=getsum(i)
    visited[x]=False
    return sumn[x]

n,m=map(int,input().split())
node=[]
edge=[]
cnt=0
while n!=0 and m!=0:
    cnt+=1
    node=list(map(int,input().split()))
    edge=[[0 for i in range(0,n)]for i in range(0,n)]
    sumn=[0 for i in range(0,n)]
    visited=[False for i in range(0,n)]
    for i in range(0,m):
        a,b=map(int,input().split())
        edge[a-1][b-1]=1
        edge[b-1][a-1]=1
    root=n//2 #随便找一点为根
    getsum(root)
    total=getsum(root)
    minn=999999999
    for i in range(0,n):
        if i!=root:
            minn=min(minn,int(abs(total-2*sumn[i])))
    print("Case "+str(cnt)+": "+str(minn))
    n,m=map(int,input().split())