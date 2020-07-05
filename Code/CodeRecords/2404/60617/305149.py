head=[]
fa=[]
x=y=0
w=[]
edges=[]
ans=0
k=0
class node(object):
    def __init__(self):
        self.u=0
        self.v=0

def dfs(x, dis,s):
    global ans
    if dis>s:
        return
    if dis==s:
        ans+=1
        return
    i=head[x]
    while i>0:
        nxt=edges[i].v
        if fa[x]!=nxt:
            dfs(nxt,dis+w[nxt],s)
        i=edges[i].u

def add_edge(x,y):
   global k
   global edges
   k+=1
   edges[k].u=head[x]
   edges[k].v=y
   head[x]=k

if __name__=='__main__':
    row=input().split(" ")
    N=int(row[0])
    S=int(row[1])
    w=[ 0 for i in range(N+1)]
    fa=[0 for i in range(N+1)]
    head=[0 for i in range(N+1)]
    row=input().split(" ")
    for i in range(1,N+1):
        w[i]=int(row[i-1])
    edges=[node() for i in range(2*N)]
    for i in range(0,N-1):
        row=input().split(" ")
        add_edge(int(row[0]),int(row[1]))
        fa[int(row[1])]=int(row[0])
    for i in range(1,N+1):
        dfs(i,w[i],S)
    print(ans)