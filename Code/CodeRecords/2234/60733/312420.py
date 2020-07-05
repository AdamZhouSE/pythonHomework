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
        minmoney[c]=min(minmoney[c],value[top])
        while top!=cur:
            top = stack.pop()
            color[top]=c
            minmoney[c]=min(minmoney[c],value[top])



n=int(input())
p = int(input())
graph = {}
low = [0 for x in range(n+1)]
dfn = [0 for x in range(n+1)]
value = [0x3f3f3f3f for x in range(n+1)]
stack = []
color = [ 0 for x in range(n+1)]
minmoney = [0x3f3f3f3f for x in range(n+1)]
c=0
time=0
an = 0
for i in range(p):
    li = [int(x) for x in input().split()]
    value[li[0]]=li[1]
m = int(input())
for i in range(m):
    f,t=[int(x) for x in input().split()]
    add_edge(f,t)

# print("graph %s"%str(graph))

for i in range(1,n+1):
    if dfn[i]==0 and value[i]!=0x3f3f3f3f:
        tarjan(i,-1)
# print("low %s"%str(low))
# print("dfn %s"%str(dfn))
# print("color %s"%str(color))
# print("value %s"%str(value))
# print("min money %s"%str(minmoney))
for i in range(1,n+1):
    if dfn[i]==0:
        print("NO")
        print(i)
        exit()
indegree = [0 for x in range(c+1)]
ans = 0
for fr,tolist in graph.items():
    for to in tolist:
        if(color[to]!=color[fr]):
            indegree[color[to]]+=1
# print("indegree %s"%str(indegree))
for i in range(1,c+1):
    if indegree[i] ==0:
        ans+=minmoney[i]
print("YES")
print(ans)