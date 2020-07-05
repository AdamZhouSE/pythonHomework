def edge(f,t):
    if f not in g:
        g[f]=[t]
    elif t not in g[f]:
        g[f].append(t)

def tarjan(cu,pre):
    global time,c
    time+=1
    low[cu]=dfn[cu]=time
    stack.append(cu)
    if cu  in g:
        for to in g[cu]:
            if dfn[to]==0:
                tarjan(to,cu)
                low[cu]=min(low[cu],low[to])
            elif to in stack:
                low[cu] = min(low[cu],dfn[to])
    if low[cu]==dfn[cu]:
        c += 1
        top = stack.pop()
        color[top]=c
        Min[c]=min(Min[c],value[top])
        while top!=cu:
            top = stack.pop()
            color[top]=c
            Min[c]=min(Min[c],value[top])

n=int(input())
p = int(input())
g = {}
low = [0 for x in range(n+1)]
dfn = [0 for x in range(n+1)]
value = [20000 for x in range(n+1)]
stack = []
color = [ 0 for x in range(n+1)]
Min = [20000 for x in range(n+1)]
c=0
time=0
an = 0
for i in range(p):
    li = [int(x) for x in input().split()]
    value[li[0]]=li[1]
m = int(input())
for i in range(m):
    f,t=[int(x) for x in input().split()]
    edge(f,t)


for i in range(1,n+1):
    if dfn[i]==0 and value[i]!=20000:
        tarjan(i,-1)
for i in range(1,n+1):
    if dfn[i]==0:
        print("NO")
        print(i)
        exit()
indegree = [0 for x in range(c+1)]
ans = 0
for fr,tolist in g.items():
    for to in tolist:
        if(color[to]!=color[fr]):
            indegree[color[to]]+=1
for i in range(1,c+1):
    if indegree[i] ==0:
        ans+=Min[i]
print("YES")
print(ans)