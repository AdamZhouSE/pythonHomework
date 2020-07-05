def add_edge(f,t):
    if f not in graph:
        graph[f]=[t]
    elif t not in graph[f]:
        graph[f].append(t)

def tarjan(cur,pre):
    global time
    time+=1
    low[cur]=dfn[cur]=time   
    child = 0
    for to in graph[cur]:
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

def dfs(cur):
    global cnt,num
    visited[cur]=T
    if(cut[cur] or cur not in graph):
        return
    cnt+=1
    for to in graph[cur]:
        if cut[to] and visited[to]!=T:
            num+=1
            visited[to]=T
        if visited[to]==0:
            dfs(to)


case=0
while True:
    case+=1
    n=int(input())
    if n == 0:
        break
    graph = {}
    low = [0 for x in range(n+2)]
    dfn = [0 for x in range(n+2)]
    cut = [False for x in range(n+2)]
    degree = [0 for x in range(n+2)]
    visited = [0 for x in range(n+2)]
    time=0
    ans1=0
    ans2=1
    T=0
    num=0
    cnt=0
    m = -1
    for i in range(n):
        f,t = [int(x) for x in input().split()]
        add_edge(f,t)
        add_edge(t,f)
        m = max(m,f,t)
    # print("graph %s"%str(graph))
    tarjan(1,-1)

    for i in range(1,m+1):
        if visited[i]==0 and cut[i]==0:
            T+=1
            cnt=num=0
            dfs(i)
            if num==0:
                ans1+=2
                ans2*=cnt*(cnt-1)/2
            if num==1:
                ans1+=1
                ans2*=cnt
    print("Case %d: %d %d"%(case,ans1,ans2))