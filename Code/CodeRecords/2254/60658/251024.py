def add_edge(f,t):
    if f not in graph:
        graph[f]=[t]
    elif t not in graph[f]:
        graph[f].append(t)

def tarjan(cur,pre):
    global time
    time+=1
    low[cur]=dfn[cur]=time   
    for to in graph[cur]:
        if to==pre:
            continue
        if dfn[to]==0:
            tarjan(to,cur)
            low[cur]=min(low[cur],low[to])
        elif dfn[to]<dfn[cur]:
            low[cur] = min(low[cur],dfn[to])

n,m=[int(x) for x in input().split()]
graph = {}
low = [0 for x in range(n+1)]
dfn = [0 for x in range(n+1)]
time=0
degree = [0 for x in range(n+1)]
ans = 0
for i in range(m):
    f,t = [int(x) for x in input().split()]
    add_edge(f,t)
    add_edge(t,f)
# print("graph %s"%str(graph))
tarjan(1,0)
# print("low %s"%str(low))
for fr,tolist in graph.items():
    for to in tolist:
        if(low[to]!=low[fr]):
            degree[low[to]]+=1
# print("degree %s"%str(degree))
for i in degree:
    if i ==1:
        ans+=1
print(int((ans+1)/2))