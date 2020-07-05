N=3005
M=8005
r,x,y,num,tot,tp,cnt=0,0,0,0,0,0,0,0,0
hd,nxt,to,dfn,low,stk,c,pr,f,vs,v=[],[],[],[],[],[],[],[],[],[],[]
def Add(x,y):
    global tot
    tot+=1
    nxt[tot]=hd[x]
    hd[x]=tot
    to[tot]=y
def Tarjan(x):
    global tot,tp,cnt
    tot+=1
    dfn[x]=low[x]=tot
    tp+=1
    stk[tp]=x
    i=hd[x]
    while(i):
        if not dfn[to[i]]:
            Tarjan(to[i])
            low[x]=min(low[x],low[to[i]])
        elif not c[to[i]]:
            low[x]=min(low[x],dfn[to[i]])
        i=nxt[i]
    if low[x]==dfn[x]:
        cnt+=1
        c[x]=cnt
        f[cnt]=pr[x]
        while(stk[tp]!=x):
            f[cnt]=min(f[cnt],pr[stk[tp]])
            tp-=1
            c[stk[tp]]=cnt
        tp-=1
def DFS(x):
    v[x]=1
    i=hd[x]
    while(i):
        if not v[to[i]]:
            DFS(to[i])
        i=nxt[i]
n=int(input())
p=int(input())
for i in range(n+1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    