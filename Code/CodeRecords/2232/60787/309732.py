def add_edge(f,t):
    if f not in graph:
        graph[f]=[t]
    elif t not in graph[f]:
        graph[f].append(t)

def tarjan(cur,pre):
    global time,c
    time+=1
    low[cur]=dfn[cur]=time
    stack.append(cur)
    if cur  in graph:
        for to in graph[cur]:
            if dfn[to]==0:
                tarjan(to,cur)
                low[cur]=min(low[cur],low[to])
            elif to in stack:#能访问到祖先节点low[to]<dfn[cur]也可
                low[cur] = min(low[cur],dfn[to])#low[to],low[cur]也可
    if low[cur]==dfn[cur]:
        c += 1
        top = stack.pop()
        color[top]=c
        while top!=cur:
            top = stack.pop()
            color[top]=c


n=int(input())
graph = {}
low = [0 for x in range(n+1)]
dfn = [0 for x in range(n+1)]
stack = []
color = [ 0 for x in range(n+1)]
c=0
time=0
ans1 = 0
ans2 = 0
for i in range(n):
    li = [int(x) for x in input().split()]
    for j in li:
        if j!=0:
            add_edge(i+1,j)
# print("graph %s"%str(graph))
for i in range(1,n+1):
    if dfn[i]==0:
        tarjan(i,-1)
indegree = [0 for x in range(c+1)]
outdegree = [0 for x in range(c+1)]
# print("low %s"%str(low))
# print("dfn %s"%str(dfn))
# print("color %s"%str(color))
for fr,tolist in graph.items():
    for to in tolist:
        if(color[to]!=color[fr]):
            indegree[color[to]]+=1
            outdegree[color[fr]]+=1
# print("indegree %s"%str(indegree))
# print("outdegree %s"%str(outdegree))
for i in indegree[1:]:
    if i ==0:
        ans1+=1
for i in outdegree[1:]:
    if i == 0:
        ans2 +=1
ans2 = ans2 if ans2>ans1 else ans1
if c==1:
    ans2=0
print(ans1)
print(ans2)