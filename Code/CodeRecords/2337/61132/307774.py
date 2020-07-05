def bfs(s):
    global level 
    level = [-1 for x in range(sink+1)]
    level[s]=0
    que = [s]
    while len(que)>0:
        f = que.pop(0)
        for to,weight,reverse in graph[f]:
            if weight>0 and level[to]<0:
                level[to]=level[f]+1
                que.append(to)
    return level

def dfs(s,t,f):
    if s==t:
        return f
    for i in graph[s]:
        if i[1]>0 and level[s]<level[i[0]]:
            d = dfs(i[0],t,min(f,i[1]))
            if d>0:
                i[1]-=d
                graph[i[0]][i[2]][1]=graph[i[0]][i[2]][1]+d
                return d
    return 0            

def dinic(s,t):
    flow = 0
    while True:
        bfs(s)
        if(level[t]<0):
            return flow
        f = dfs(s,t,0x22222222)
        while f>0:
            flow+=f
            f = dfs(s,t,0x22222222)

def createnode(x,y):
    return x*c+y

def edge(f,t,w):
    if f not in graph:
        graph[f] = []
    if t not in graph:
        graph[t] = []
    graph[f].append([t,w,len(graph[t])])
    graph[t].append([f,0,len(graph[f])-1])

r,c = [int(x) for x in input().split()]
so = [list(input()) for x in range(r)]
tmpr = -1
tmpc = -1
rNO=[0 for x in range(c*r)]
cNO=[0 for x in range(c*r)]
for i in range(r):
    for j in range(c):
        if so[i][j]=="#":
            continue
        if j==0 or so[i][j-1]=="#":
            tmpr+=1
        rNO[createnode(i,j)]=tmpr
for j in range(c):
    for i in range(r):
        if so[i][j]=="#":
            continue
        if i==0 or so[i-1][j]=="#":
            tmpc+=1
        cNO[createnode(i,j)]=tmpc
source = tmpc*tmpr+1
sink = tmpc*tmpr+2
level = []
graph ={}
for i in range(tmpr+1):
    edge(source,i,1)
for i in range(tmpc+1):
    edge(1+i+tmpr,sink,1)

for i in range(r):
    for j in range(c):
        if so[i][j]=="*":
            edge(rNO[createnode(i,j)],1+tmpr+cNO[createnode(i,j)],1)

ans = 0
ans+=dinic(source,sink)
print(ans,end="")