class Graph:
    def __init__(self,matrix):
        self.matrix=matrix
def near(graph,a):
    re=[]
    for i in range(len(graph.matrix)):
        if graph.matrix[a-1][i]>0:
            re.append(i+1)
    return re
        
def prim(graph,a):
    n=len(graph.matrix)
    Vn=[]
    re=0
    Vn.append(a)
    k=0
    while(k!=n-1):
        minedge=1000000000000000000000
        minp=-1
        for i in range(len(Vn)):
            for j in range(n):
                if graph.matrix[Vn[i]-1][j]<minedge and graph.matrix[Vn[i]-1][j]>0:
                    if Vn.count(j+1)==0:
                        minedge=graph.matrix[Vn[i]-1][j]
                        minp=j+1
        if minp==-1:
            return -1
        else:
            Vn.append(minp)
            re+=minedge
        k+=1
    return re        

li=input().split()
n=int(li[0])
m=int(li[1])
t1=[]
g=[]
for i in range(n):
    t1.append(-1)
for i in range(n):
    t1=t1[:]
    g.append(t1)
for i in range(m):
    li=list(map(int,input().split()))
    g[li[0]-1][li[1]-1]=li[2]
for i in range(n):
    g[i][i]=0
graph=Graph(g)
re=-1
for i in range(1,n+1):
    tmp=prim(graph,i)
    if tmp!=-1 and (tmp<re or re==-1):
        re=tmp
print(re)
        

    