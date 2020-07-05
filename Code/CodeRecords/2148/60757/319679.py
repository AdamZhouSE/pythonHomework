class Graph:
    def __init__(self,matrix):
        self.matrix=matrix
def near(graph,a):
    re=[]
    for i in range(len(graph.matrix)):
        if graph.matrix[a-1][i]>0:
            re.append(i+1)
    return re
        
def dij(graph,a,b,k,sale):
    n=len(graph.matrix)
    li=[]
    for i in range(2*k+1):
        li.append(-1)
    re=[]
    for i in range(n):
        li=li[:]
        re.append(li)
    li=[]
    for i in range(2*k+1):
        li.append(0)
    sure=[]
    for i in range(n):
        li=li[:]
        sure.append(li)
    if sale[a-1]==1:
        re[a-1][k-1]=0
        sure[a-1][k-1]=1
        com=k-1
    else:
        re[a-1][k+1]=0
        sure[a-1][k+1]=1
        com=k+1
    tmp=a
    bind=-1
    while(True):
        for i in range(n):
            if graph.matrix[tmp-1][i]>0:
                if sale[i]==1:
                    tm=-1
                else:
                    tm=1
                if com+tm<2*k+1 and com+tm>-1:
                    if re[i][com+tm]==-1 or re[tmp-1][com]+graph.matrix[tmp-1][i]<re[i][com+tm]:
                        re[i][com+tm]=re[tmp-1][com]+graph.matrix[tmp-1][i]
        minindi=-1
        minindj=-1
        minl=-1
        for i in range(n):
            for j in range(2*k+1):
                if sure[i][j]==0:
                    if re[i][j]>0:
                        if minl==-1 or re[i][j]<minl:
                            minl=re[i]
                            minindi=i
                            minindj=j
        if minl==-1:
            break
        sure[minindi][minindj]=1
        tmp=minindi+1
        com=minindj
        for i in range(2*k-1):
            if sure[b-1][i]==1:
                bind=i
                break
    if bind==-1:
        return -1
    else:
        return re[b-1][bind]        
    
T=int(input())
for r in range(T):
    li=input().split()
    n=int(li[0])
    m=int(li[1])
    k=int(li[2])
    sale=list(map(int,input().split()))
    t1=[]
    time=[]
    for i in range(n):
        t1.append(-1)
    for i in range(n):
        t1=t1[:]
        time.append(t1)
    for i in range(m):
        li=list(map(int,input().split()))
        time[li[0]-1][li[1]-1]=li[2]
    for i in range(n):
        time[i][i]=0
    graph=Graph(time)
    li=input().split()
    a=int(li[0])
    b=int(li[1])
    tmp=dij(graph,a,b,k,sale)
    print(tmp)
    