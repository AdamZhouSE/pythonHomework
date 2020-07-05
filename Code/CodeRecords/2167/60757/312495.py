class Graph:
    def __init__(self,matrix):
        self.matrix=matrix
def near(graph,a):
    re=[]
    for i in range(len(graph.matrix)):
        if graph.matrix[a-1][i]>0:
            re.append(i+1)
    return re
        
def dij(graph,a):
    n=len(graph.matrix)
    re=[]
    for i in range(n):
        re.append(-1)
    sure=[]
    for i in range(n):
        sure.append(0)
    re[a-1]=0
    sure[a-1]=1
    tmp=a
    k=0
    while(k!=n-1):
        for i in range(n):
            if graph.matrix[tmp-1][i]>0:
                if re[i]==-1 or re[tmp-1]+graph.matrix[tmp-1][i]<re[i]:
                        re[i]=re[tmp-1]+graph.matrix[tmp-1][i]
        minind=-1
        minl=-1
        for i in range(n):
            if sure[i]==0:
                if re[i]>0:
                    if minl==-1 or re[i]<minl:
                        minl=re[i]
                        minind=i
        sure[minind]=1
        tmp=minind+1
        k+=1

    return re        

li=input().split()
n=int(li[0])
m=int(li[1])
L=int(li[2])
color=list(map(int,input().split()))
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
    g[li[1]-1][li[0]-1]=li[2]
for i in range(n):
    g[i][i]=0
graph=Graph(g)
add=[]
for i in range(n-1):
    for j in range(i+1,n):
        if abs(color[i]-color[j])>=L and g[i][j]!=-1:
            add.append([i+1,j+1])
re=0
for i in range(len(add)):
    li=dij(graph,add[i][0])
    re+=li[add[i][1]-1]
print(re)
        

    