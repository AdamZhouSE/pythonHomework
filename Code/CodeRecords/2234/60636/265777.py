N=3005
M=8005
x,y,tot,tp,cnt=0,0,0,0,0
hd,nxt,to,dfn,low,stk,c,pr,f,vs,v=[],[],[],[],[],[],[],[],[],[],[]
def memset (source):
    res=[]
    for i in range(M):
        if(source==""):
            a=[]
            res.append(a)
        else:
            res.append(source)
    return res
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
hd=memset(0)
nxt=memset(0)
to=memset(0)
dfn=memset(0)
low=memset(0)
stk=memset(0)
c=memset(0)
pr=memset(0)
f=memset(0)
vs=memset(0)
v=memset(0)
n=int(input())
p=int(input())
for i in range(1,n+1):
    pr[i]=N
for i in range(1,p+1):
    w=input().split(" ")
    x=int(w[0])
    y=int(w[1])
    pr[x]=y
r=int(input())
for i in range(1,r+1):
    w=input().split(" ")
    x=int(w[0])
    y=int(w[1])
    Add(x,y)
for i in range(1,n+1):
    if pr[i]<N and not v[i]:
        DFS(i)
for i in range(1,n+1):
    if not v[i]:
        print("NO")
        print(i)
        break
for i in range(1,n+1):
    if not c[i]:
        Tarjan(i)
for i in range(1,n+1):
    j=hd[i]
    while(j):
        if c[i]!=c[to[j]]:
            vs[c[to[j]]]=1
        j=nxt[j]
    ans=0
    for i in range(1,cnt+1):
        if not vs[i]:
            ans+=f[i]
    print("YES")
    print(ans)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    