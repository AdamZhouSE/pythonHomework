aa=eval(input())
while aa!=0:
    head=[-1 for x in range(aa)]
    df=[-1 for x in range(aa)]
    low=[-1 for x in range(aa)]
    cut=set()
    belong=[-1 for x in range(aa)]
    edgeArray=[]
    def addEdge(u,v,w):
        global edgeArray,head
        edgeArray.append([v,w,head[u]])
        head[u]=len(edgeArray)-1
    a=[int(x)-1 for x in input().split()]
    while len(a)!=1:
        u=a[0]
        for v in a[1:]:
            addEdge(u,v,0)
            addEdge(v,u,0)
        a=[int(x)-1 for x in input().split()]
    root=0
    def dfs(i,depth,path:list,fa):
        global df,low,belong,cut,root
        df[i]=depth
        low[i]=depth
        path.append(i)
        next=head[i]
        while next!=-1:
            node=edgeArray[next][0]
            if node==fa:
                pass
            elif df[node]==-1:
                dfs(node,depth+1,path,i)
                low[i]=min(low[i],low[node])
                if low[node]>=df[i]:
                    if root==i:
                        root=-1
                    else:
                        cut.add(i)
                    t=path.pop()
                    while t!=i:
                        t=path.pop()
                    path.append(t)
            elif node in path:
                low[i] = min(low[i], low[node])
            next=edgeArray[next][2]

    dfs(0,0,[],-1)
    print(len(cut))
    aa = eval(input())



