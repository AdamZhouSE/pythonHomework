def add_edge(u,v):
    if u not in graph:
        graph[u]=[v]
    elif v not in graph[u]:
        graph[u].append(v) 

def tarjan(v):
    global time,c
    time+=1
    low[v]=dfn[v]=time
    stack.append(v)
    if v in graph:
        for to in graph[v]:
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




n = int(input())
low = [0 for x in range(n)]
stack = []
color = [0 for x in range(n)]
dfn = [0 for x in range(n)]
degree = {}
c = 0
num={}
graph = {}
ans = 0
time = 0
temp = 0
edges=[]
for i in range(n):
    edges.append(input().split())
for i in range(n):
    for j in range(n):
        if edges[i][j]=="1":
            add_edge(i,j)
# print(graph)
for i in range(n):
    if dfn[i]==0:
        tarjan(i)
degree = [0 for x in range(c)]
for cur,tolist in graph.items():
    for to in tolist:
        if color[cur]!=color[to]:
                degree[color[to]]+=1
# print(degree)
for i in range(c):
    if degree[i]==0:
        ans+=1
print(ans)