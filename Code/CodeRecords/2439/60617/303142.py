visit=[]
head=[]
edges=[]
k=0
dis=[]

class edge(object):
    def __init__(self):
        self.to=0
        self.next=0
        self.weight=0

def add_Edge(u,v,w):
    global k
    k=k+1
    edges[k].to=v
    edges[k].next=head[u]
    edges[k].weight=w
    head[u]=k

def dfs(idx,val):
    global dis
    global visit
    dis[idx]=val
    visit[idx]=True
    i=head[idx]
    while i!=0:
        if not visit[edges[i].to]:
            dfs(edges[i].to,val^edges[i].weight)
        i=edges[i].next

if __name__=='__main__':
    k = 0
    N=int(input())
    edges=[edge() for i in range(0,2*N+1)]
    head=[0 for i in range(0, 2*N+1)]
    dis=[0 for i in range(0,2*N+1)]
    visit=[False for i in range(0,2*N+1)]
    for i in range(0,N-1):
        row=list(map(int,input().split(" ")))
        add_Edge(row[0],row[1],row[2])
        add_Edge(row[1],row[0],row[2])
    M=int(input())
    query_Li=[]
    dfs(1,0)
    for i in range(0,M):
        query_Li.append(list(map(int,input().split(" "))))
    for query in query_Li:
        print(dis[query[0]]^dis[query[1]])
