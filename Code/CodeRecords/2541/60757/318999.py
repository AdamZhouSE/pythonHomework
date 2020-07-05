class Graph:
    def __init__(self,matrix):
        self.matrix=matrix
def near(graph,a):
    re=[]
    for i in range(len(graph.matrix)):
        if graph.matrix[a-1][i]>0:
            re.append(i+1)
    return re
        
def p(graph,study,rel):
    n=len(graph.matrix)
    tmp=[]
    for i in range(len(rel)):
        tmp.append(rel[i][0])
    re=[]
    for i in range(n):
        if tmp.count(i)==0:
            re.append(i)
            study[i]=1
    tt=len(re)
    k=0
    quene=re[:]
    while(k!=n-tt):
        a=quene.pop(0)
        for j in range(n):
            if graph.matrix[a][j]==1:
                tmp=[]
                for i in range(len(rel)):
                    if rel[i][0]==j:
                        tmp.append(rel[i][1])
                sign=0
                for i in range(len(tmp)):
                    if study[tmp[i]]==0:
                        sign=1
                if sign==1:
                    continue
                else:
                    study[j]=1
                    quene.append(j)
                    re.append(j)
        k+=1
    return re

n=int(input())
rel=eval(input())
study=[]
t1=[]
g=[]
for i in range(n):
    t1.append(-1)
    study.append(0)
for i in range(n):
    t1=t1[:]
    g.append(t1)
for i in range(len(rel)):
    tmp=rel[i]
    g[tmp[1]][tmp[0]]=1
for i in range(n):
    g[i][i]=0
graph=Graph(g)
re=p(graph,study,rel)
tmp=re[:]
if len(list(tuple(set(tmp))))<len(re):
    print('0')
else:
    print(re)
        

    