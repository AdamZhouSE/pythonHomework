def tarjan(v):
    global time,c
    time+=1
    low[v]=dfn[v]=time
    stack.append(v)
    if v in g:
        for to in g[v]:
            if dfn[to]==0:
                tarjan(to)
                low[v]=min(low[to],low[v])
            elif to in stack:
                low[v]=min(low[to],low[v])
    if low[v]==dfn[v]:
        top = stack.pop()
        color[top]=c
        if c not in num:
            num[c]=1
        while top!=v:
            top=stack.pop()
            color[top]=c
            num[c]+=1
        c+=1
def edge(u,v):
    if u not in g:
        g[u]=[v]
    elif v not in g[u]:
        g[u].append(v)
n = int(input())
low = [0 for x in range(n)]
stack = []
color = [0 for x in range(n)]
dfn = [0 for x in range(n)]
degree = {}
c = 0
num={}
g = {}
ans = 0
time = 0
temp = 0
edges=[]
for i in range(n):
    edges.append(input().split())
for i in range(n):
    for j in range(n):
        if edges[i][j]=="1":
            edge(i,j)
for i in range(n):
    if dfn[i]==0:
        tarjan(i)
degree = [0 for x in range(c)]
for cur,tolist in g.items():
    for to in tolist:
        if color[cur]!=color[to]:
                degree[color[to]]+=1
for i in range(c):
    if degree[i]==0:
        ans+=1
print(ans)