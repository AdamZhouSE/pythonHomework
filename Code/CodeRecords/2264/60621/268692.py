aa=eval(input())
case=0
while aa!=0:
    case+=1
    a=2*aa
    df=[-1 for i in range(a)]
    low=[-1 for i in range(a)]
    belong=[-1 for i in range(a)]
    index=-1
    belongArray=[]
    edgeArray=[]
    head=[-1 for i in range(a)]
    def addEge(u,v,w):
        global edgeArray
        edgeArray.append([v,w,head[u]])
        head[u]=len(edgeArray)-1
    x={}
    for i in range(aa):
        trmp=[int(x)-1 for x in  input().split()]
        addEge(trmp[0],trmp[1],0)
        addEge(trmp[1],trmp[0],0)
    root=0
    cut=set()
    def dfs(i,depth,path:list,fa):
        global df,low,belong,belongArray,index,cut,root

        df[i]=depth
        low[i]=depth
        next=head[i]
        path.append(i)
        while next!=-1:
            node=edgeArray[next][0]
            if node==fa:
                pass
            elif df[node]==-1:
                dfs(node,depth+1,path,i)
                low[i]=min(low[i],low[node])
                if low[node] >= df[i]:
                    if i!=root:
                        cut.add(i)
                    else:
                        root=-1
                    index += 1
                    temp = [i]
                    belong[i] = index
                    t = path.pop()
                    while t != i:
                        temp.append(t)
                        belong[t] = index
                        t = path.pop()
                    belongArray.append([x for x in temp])
                    path.append(i)
            elif node in path:
                low[i] = min(low[i], low[node])
            next=edgeArray[next][2]


    dfs(0,0,[],-1)
    ans=[0,1]
    for i in belongArray:
        total=0
        for k in i:
            if k in cut:
                total+=1
        if total<1:
            ans[0]+=2
            ans[1]*=(len(i)*(len(i)-1)//2)
        elif total==1:
            ans[0]+=1
            ans[1]*=(len(i)-1)


    st="Case "+str(case)+": "+str(ans[0])+" "+str(ans[1])
    print(st)
    aa = eval(input())
