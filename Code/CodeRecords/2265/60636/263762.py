n,m,ans,cnt=0,0,0,0
low=[]
dfn=[]
par=[]
ap=[]
mp=[]
N=10005
def memset (source):
    res=[]
    for i in range(N):
        if(source==""):
            a=[]
            res.append(a)
        else:
            res.append(source)
    return res
def init():
    global ans,cnt,low,par,ap,mp
    ans=0
    cnt=0
    low=memset(0)
    dfn=memset(0)
    par=memset(0)
    ap=memset(0)
    mp=memset("")
def tarjan(u):
    global cnt
    cnt+=1
    dfn[u]=low[u]=cnt
    son=0
    for i in range(len(mp[u])):
        v=mp[u][i]
        if not dfn[v]:
            son+=1
            par[v]=u
            tarjan(v)
            low[u]=min(low[u],low[v])
            if dfn[u]==1 and son>1 and not ap[u]:
                ap[u]=1
                ans+=1
            elif dfn[u]!=1 and low[v]>=dfn[u] and not ap[u]:
                ap[u]=1
                ans+=1
        elif par[v]!=u:
            low[u]=min(low[u],dfn[v])
while(True):
    x=int(input())
    if x==0:
        break
    else:
        while(True):
            init()
            x=input()
            print(dfn)
            if(x=="0"):
                break
            else:
                x=x.split(" ")
                a=int(x[0])
                for i in range(1,len(x)):
                    b=int(x[i])
                    mp[a].append(b)
                    mp[b].append(a)
        tarjan(1)
        print(ans)
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                