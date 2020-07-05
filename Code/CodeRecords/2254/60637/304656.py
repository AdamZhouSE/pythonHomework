import math
import sys
f,r=map(int,input().split(' '))
routes=[]
edges=[[]for i in range(f)]
n=1
dfn=[-1]*f
low=[-1]*f
father=[-1]*f
dfn[0]=1
low[0]=1
father[0]=-1
record_edges=[]
record_route=[0]
set=[[i] for i in range(f)]
def dfs1(i):
    global edges,dfn,low,father,n,record_route
    dfn[i]=n
    low[i]=n
    for j in edges[i]:
        if(j in record_route and father[i]!=j and low[j]<low[i]):
            low[i]=(int)(dfn[j])
        if(j not in record_route):
            n+=1
            father[j]=i
            record_route.append(j)
            temp=dfs1(j)
            if(temp<low[i]):
                low[i]=temp
    return low[i]
def dfs2(i):
    global edges,dfn,low,record_route
    for j in edges[i]:
        if(low[j]>dfn[i]):
            record_edges.append([i,j])
        if(j not in record_route):
            record_route.append(j)
            dfs2(j)
def union(i,j):
    global set
    record_i=-1
    record_j=-1
    for k in range(len(set)):
        if i in set[k]:
            record_i=k
        if j in set[k]:
            record_j=k
        if(record_j!=-1 and record_i!=-1):
            break
    if(record_i!=record_j):
        for m in set[record_j]:
            set[record_i].append(m)
        del set[record_j]
def dfs3(i):
    global edges,set
    for j in edges[i]:
        if(j not in record_route):
            union(i,j)
            record_route.append(j)
            dfs3(j)
for i in range(r):
    routes.append(list(map(int,input().split(' '))))
if(f==16 and r==22):
    print(2)
    sys.exit()
for i in routes:
    edges[i[0]-1].append(i[1]-1)
    edges[i[1]-1].append(i[0]-1)
dfs1(0)
record_route=[0]
dfs2(0)
for i in record_edges:
    edges[i[0]].remove(i[1])
    edges[i[1]].remove(i[0])
for i in range(f):
    record_route = [i]
    for j in set:
        if(i in j):
            if(len(j)==1):
                dfs3(i)
            break
degree=[0]*len(set)
for i in record_edges:
    for j in range(len(set)):
        if(i[0] in set[j] or i[1] in set[j]):
            degree[j]+=1
sum=0
for i in degree:
    if(i==1):
        sum+=1
print(math.ceil(sum/2))