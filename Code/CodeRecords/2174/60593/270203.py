class Node:
    def __init__(self):
        self.nxt,self.to,self.w,self.valid=0,0,0,False
def addEdge(u,v,w):
    global cnt
    cnt+=1
    e[cnt].nxt=head[u]
    e[cnt].w=w
    e[cnt].to=v
    e[cnt].valid=True
    head[u]=cnt
def delEdge(u,v):
    i=head[u]
    while(i):
        if(e[i].to==v):
            e[i].valid=False
            break
        i=e[i].nxt
def dijkstra(s):
    Q=[]
    dist[s]=0
    Q.append(s)
    while(len(Q)):
        p=Q[0]
        del Q[0]
        i=head[p]
        while(i):
            E=e[i]
            if(E.valid and dist[E.to]>max(dist[p],E.w)):
                dist[E.to]=max(dist[p],E.w)
                if(E.to not in Q):
                    Q.append(E.to)
            i=e[i].nxt

n,q=map(int,input().split())
N=n+5
e=[Node()for i in range(N<<3)]
cnt,head,vis=0,[0]*N,[False]*N

for _ in range(q):
    qq=list(map(int,input().split()))
    if(qq[0]==0):
        addEdge(qq[1],qq[2],qq[3])
        addEdge(qq[2],qq[1],qq[3])
    elif(qq[0]==1):
        delEdge(qq[1],qq[2])
        delEdge(qq[2],qq[1])
    else:
        dist=[float('inf')]*N
        dijkstra(qq[1])
        print(-1 if dist[qq[2]]==float('inf') else dist[qq[2]])