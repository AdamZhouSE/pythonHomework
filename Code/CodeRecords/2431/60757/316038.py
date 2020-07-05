import math
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
    re=[]
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
            re.append(minedge)
        k+=1
    return re        

li=input().split()
s=int(li[0])
n=int(li[1])
t1=[]
g=[]
for i in range(n):
    t1.append(-1)
for i in range(n):
    t1=t1[:]
    g.append(t1)
posi=[]
for i in range(n):
    li=list(map(int,input().split()))
    posi.append(li)    
for i in range(n-1):
    for j in range(i+1,n):
        x1,y1=posi[i][0],posi[i][1]
        x2,y2=posi[j][0],posi[j][1]
        dis=math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
        dis=round(dis,2)
        g[i][j]=dis
        g[j][i]=dis
for i in range(n):
    g[i][i]=0
graph=Graph(g)
re=-1
re=prim(graph,1)
re=sorted(re)
print('%.2f'%re[len(re)-s],end='')
        

    