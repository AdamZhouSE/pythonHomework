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




n,m = [int(x) for x in input().split()]
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
for i in range(m):
    a,b=[int(x)-1 for x in input().split()]
    add_edge(a,b)
# print(graph)
for i in range(n):
    if dfn[i]==0:
        tarjan(i)
degree = [0 for x in range(c)]
for cur,tolist in graph.items():
    for to in tolist:
        if color[cur]!=color[to]:
                degree[color[cur]]+=1
# print(degree)
for i in range(c):
    if degree[i]==0:
        temp+=1
        ans = i
    if temp>=2:
        print(0)
        exit()
# print(num)
# print(ans)
print(num[ans])