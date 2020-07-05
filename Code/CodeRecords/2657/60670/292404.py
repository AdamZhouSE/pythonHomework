def search(x):
    global n,edge,signed
    if signed[x]:
        return x
    for i in range(1,n+1):
        if edge[x][i]==1:
            return search(i)

n,q=map(int,input().split())
edge=[[0 for i in range(0,n+1)]for i in range(0,n+1)]
for i in range(0,n-1):
    u,v=map(int,input().split())
    edge[v][u]=1 # 反向做边 
signed=[False for i in range(0,n+1)]
signed[1]=True
for i in range(0,q):
    op=input().split()
    num=int(op[1])
    if op[0]=='Q':
        print(search(num))
    else:
        signed[num]=True