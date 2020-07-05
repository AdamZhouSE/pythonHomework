def memset(a,length):
    res=[]
    for i in range(length):
        res.append(a)
    return res
def ADD(x,y,en,tot,nex,las):
    en[++tot]=y
    nex[tot]=las[x]
    las[x]=tot
def Tarjan(x,f,dfn,low,VT,en,nex,las,Cut):
    VT+=1
    dfn[x]=VT
    low[X]=VT
    i,y,son=0,0,0
    i=las[x]
    while(i):
        y=en[i]
        if not dfn[y]:
            Tarjan(y,x,dfn,low,VT,en,nex,las,Cut)
            son+=1
            low[x]=min(low[x],low[y])
            if low[y]>=dfn[x] and f:
                Cut[x]=True
        elif y!=f:
            low[x]=min(low[x],dfn[y])
        i=nex[i]
    if f==0 and son>2:
        Cut[x]=True
def DFS(x,vis,Size,pbc,las,nex,Cut,CTime,con):
    i=las[x]
    vis[x]=True
    Size[pbc]+=1
    while(i):
        y=en[i]
        if vis[y] or Cut[y]:
            if Cut[y] and Ctime[y]!=pbc:
                con[pbc]+=1
                Ctime[y]=pbc
        DFS(y,vis,Size,pbc,las,nex,Cut,CTime,con)
n=10005
t=0
while(True):
    t+=1
    z=int(input())
    if(z==0):
        break
    else:
        VT,tot,P,pbc,Ans_cnt,Ans_tot=0,0,0,0,0,1
        las=memset(0,n)
        dfn=memset(0,n)
        low=memset(0,n)
        Cut=memset(False,n)
        mark=memset(False,n)
        vis=memset(False,n)
        be=memset(0,n)
        Size=memset(0,n)
        con=memset(0,n)
        CTime=memset(0,n)
        en=memset(0,n)
        nex=memset(0,n)
        for i in range(z):
            x_y=input().split(" ")
            x=int(x_y[0])
            y=int(x_y[1])
            ADD(x,y,en,tot,nex,las)
            ADD(y,x,en,tot,nex,las)
            P=max(P,x)
            P=max(P,y)
            mark[x]=True
            mark[y]=True
        for i in range(1,P+1):
            if not dfn[i]:
                Tarjan(i,0,dfn,low,VT,en,nex,las,Cut)
        for i in range(1,P+1):
            if mark[i] and not vis[i] and not Cut[i]:
                pbc+=1
                DFS(i,vis,Size,pbc,las,nex,Cut,CTime,con)
        for i in range(1,pbc+1):
            if con[i]==0:
                Ans_tot*=(Size[i]-1)*Size[i]/2
                Ans_cnt+=2
            elif con[i]==1:
                Ans_tot*=Size[i]
                Ans_cnt+=1
        print("Case "+str(t)+": "+str(Ans_cnt)+" "+str(Ans_tot))