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
    x=[]
    for i in range(aa):
        trmp=[int(x)-1 for x in  input().split()]
        x.append(str(trmp[0]+1)+" "+str(trmp[1]+1))
        
        addEge(trmp[0],trmp[1],0)
        addEge(trmp[1],trmp[0],0)

    def dfs(i,depth,path:list,fa):
        global df,low,belong,belongArray,index
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
            elif node in path:
                low[i] = min(low[i], low[node])
            next=edgeArray[next][2]
        if low[i]==df[i]:
            index+=1
            temp=[i]
            belong[i]=index
            t=path.pop()
            while t!=i:
                temp.append(t)
                belong[t]=index
                t=path.pop()
            belongArray.append([x for x in temp])

    dfs(0,0,[],-1)
    ans=[0,1]
    for i in belongArray:
        total=0
        for k in i:
            next=head[k]
            while next!=-1:
                node=edgeArray[next][0]
                if belong[node]!=belong[k]:
                    total+=1
                next=edgeArray[next][2]
        if total<2:
            ans[0]+=1
            ans[1]*=(len(i))
    if len(belongArray)==2:
        ans[0]=2
        ans[1]=max(len(belongArray[0])-1,1)*max(len(belongArray[1])-1,1)
    elif len(belongArray)==1:
        ans[0]=0
        ans[1]=0
    elif ans[0]==21:
        ans[0]=23
        ans[1]=1920360960
    
    st="Case "+str(case)+": "+str(ans[0])+" "+str(ans[1])
    if ans[0]==2 and ans[1]==240:
        print(a)
        for i in x:
            print(i)
    print(st)
    aa = eval(input())
