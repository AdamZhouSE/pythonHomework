class edge:
    def __init__(self):
        self.nxt=0
        self.to=0
        self.w=0

Nedges=[ edge() for i in range(2**16)]
Nhead=[0 for i in range(0, 701)]
k=0
dis=[]
def add(u,v,w):
    global k
    global Nhead
    global Nedges
    k+=1
    Nedges[k].to=v
    Nedges[k].w=w
    Nedges[k].nxt=Nhead[u]
    Nhead[u]=k

def dijkstra(k,n,edges,head):
    global dis
    dis=[float("inf") for i in range(n+1)] #初始化距离列表
    visited=[k]
    unvisited=[]
    for i in range(1,n+1):
        if i!=k:
            unvisited.append(i) #初始化unvisited列表
    i=head[k]
    while i!=0:
        to=edges[i].to
        dis[to]=edges[i].w
        i=edges[i].nxt
    #初始化dis 列表
    current=dis.index(min(dis))
    tempDis=[float("inf") for i in range(n+1)]
    i=head[current]
    while i!=0:
        to=edges[i].to
        tempDis[to]=edges[i].w
        i=edges[i].nxt
    while unvisited:
        for i in range(1,n+1):
            if i!=current and i!=k:
                dis[i]=min(dis[i],dis[current]+tempDis[i])
        visited.append(current)
        unvisited.remove(current)
        MIN=float("inf")
        MINidx=0
        for i in range(1,n+1):
            if i!=current and i in unvisited:
                if dis[i]<MIN:
                    MIN=dis[i]
                    MINidx=i
        current=MINidx
        i=head[current]
        tempDis=[float("inf") for i in range(n+1)]
        while i!=0:
            to=edges[i].to
            tempDis[to]=edges[i].w
            i=edges[i].nxt
    return dis.copy()

if __name__=='__main__':
    row=input().split(" ")
    n=int(row[0])
    m=int(row[1])
    start=int(row[2])
    a=int(row[3])
    b=int(row[4])
    for i in range(0,m):
        edge=input().split(" ")
        u=int(edge[0])
        v=int(edge[1])
        add(u,v,a)
        add(v,u,a)
    initEdges=Nedges.copy()
    initHead=Nhead.copy()
    for i in range(1,n):
        temp=dijkstra(i,n,initEdges,initHead)
        for j in range(i+1,n+1):
            if temp[j]==2*a:
                add(i,j,b)
                add(j,i,b)
    res=dijkstra(start, n, Nedges,Nhead)
    for i in range(1,n+1):
        if i==start:
            print(0)
        else:
            print(res[i])