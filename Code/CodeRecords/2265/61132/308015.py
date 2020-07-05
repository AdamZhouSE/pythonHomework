def edge(f,t):
    if f not in g:
        g[f]=[t]
    elif t not in g[f]:
        g[f].append(t)

def tarjan(cur,pre):
    global time
    time+=1
    low[cur]=dfn[cur]=time   
    child = 0
    for to in g[cur]:
        if dfn[to]==0:
            child+=1
            tarjan(to,cur)
            low[cur] = min(low[cur],low[to])
            if low[to]>=dfn[cur]:
                cut[cur]=True
        elif dfn[to]<dfn[cur] and to !=pre :
            low[cur] = min(low[cur],dfn[to])
    if pre<0 and child ==1:
        cut[cur]=False

while True:
    n=int(input())
    if n == 0:
        break
    g = {}
    low = [0 for x in range(n+1)]
    dfn = [0 for x in range(n+1)]
    cut = [False for x in range(n+1)]
    time=0
    ans=0
    while True:
        li = [int(x) for x in input().split()]
        if li[0]==0:
            break
        for i in li[1:]:
            edge(li[0],i)
            edge(i,li[0])
    tarjan(1,-1)
    print(cut.count(True))