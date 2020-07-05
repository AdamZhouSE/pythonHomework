class Graph:
    def __init__(self,matrix):
        self.matrix=matrix
def near(graph,a):
    re=[]
    for i in range(len(graph.matrix)):
        if graph.matrix[a-1][i]>0:
            re.append(i+1)
    return re
def cal(graph,a,color):
    li=near(graph,a)
    for i in range(len(li)):
        if color[li[i]-1]==color[a-1]:
            return False
        elif color[li[i]-1]==0:
            if color[a-1]==1:
                color[li[i]-1]=2
            else: 
                color[li[i]-1]=1
            return cal(graph,li[i],color)
    return True
        
T=int(input())
for r in range(T):
    li=input().split()
    n=int(li[0])
    m=int(li[1])
    t1=[]
    g=[]  
    color=[]
    for i in range(n):
        color.append(0)
        t1.append(-1)
    for i in range(n):
        t1=t1[:]
        g.append(t1)
    for i in range(m):
        li=list(map(int,input().split()))
        g[li[0]-1][li[1]-1]=1
        g[li[1]-1][li[0]-1]=1
    for i in range(n):
        g[i][i]=0
    graph=Graph(g)
    color[0]=1
    boo=cal(graph,1,color)
    if boo ==True:
        print('YES')
    else:
        print('NO')