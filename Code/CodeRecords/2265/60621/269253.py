aa=eval(input())
t=0
while aa!=0:
    t+=1
    tt=[]
    if t==13:
        tt.append(aa)
    head=[-1 for x in range(aa)]
    df=[-1 for x in range(aa)]
    low=[-1 for x in range(aa)]
    valid=[False for x in range(aa)]
    cut=set()
    belong=[-1 for x in range(aa)]
    edgeArray=[]
    def addEdge(u,v,w):
        global edgeArray,head
        edgeArray.append([v,w,head[u]])
        head[u]=len(edgeArray)-1
    if t==13:
        temp=input()
        tt.append(temp)
        a=[int(x)-1 for x in temp.split()]
    else:
        a = [int(x) - 1 for x in input().split()]
    while len(a)!=1:
        u=a[0]
        for v in a[1:]:
            addEdge(u,v,0)
            addEdge(v,u,0)
        if t == 13:
            temp = input()
            tt.append(temp)
            a = [int(x) - 1 for x in temp.split()]
        else:
            a = [int(x) - 1 for x in input().split()]
    root=0
    def dfs(i,depth,path:list,fa):
        global df,low,belong,cut,root
        # if i==19 or i==14 or i==17:
        #     print("apap")
        df[i]=depth
        low[i]=depth
        path.append(i)
        next=head[i]
        valid[i]=True
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
                low[i] = min(low[i], df[node])
            next=edgeArray[next][2]

    while not all(valid):
        root=0
        while valid[root]==True:
            root+=1
        dfs(root,0,[],-1)
    if t==13 and len(cut)==5:
        print("pause")
        for i in tt:
            print(tt)
        print("pause")


    print(len(cut))
    if t == 13 and t==-1:
        temp = input()
        tt.append(temp)
        aa = eval(temp)
    else:
        aa=eval(input())



