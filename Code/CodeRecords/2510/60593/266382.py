def addedge(x,y):
    global e
    e+=1
    to[e]=y
    nex[e]=beg[x]
    beg[x]=e

###线段树
def build(rt,l,r):
    global Mod
    if(l==r):
        a[rt]=wt[l]
        if(a[rt]>Mod):
            a[rt]%=Mod
        return
    mid=(l+r)>>1
    build(rt<<1,l,mid)
    build(rt<<1|1,mid+1,r)
    a[rt]=(a[rt<<1]+a[rt<<1|1])%Mod
def pushDown(rt,lenn):
    global Mod
    laz[rt<<1]+=laz[rt]
    laz[rt<<1|1]+=laz[rt]
    a[rt<<1]+=laz[rt]*(lenn-(lenn>>1))
    a[rt<<1|1]+=laz[rt]*(lenn>>1)
    a[rt<<1]%=Mod
    a[rt<<1|1]%=Mod
    laz[rt]=0
def query(rt,l,r,L,R):
    global res,Mod
    if(L<=l and r<=R):
        res+=a[rt]
        res%=Mod
        return
    else:
        if(laz[rt]):
            pushDown(rt,r-l+1)
        mid=(l+r)>>1
        if(L<=mid):
            query(rt<<1,l,mid,L,R)
        if(R>mid):
            query(rt<<1|1,mid+1,r,L,R)
def update(rt,l,r,L,R,k):
    global Mod
    if(L<=l and r<=R):
        laz[rt]+=k
        a[rt]+=k*(r-l+1)
    else:
        if(laz[rt]):
            pushDown(rt,r-l+1)
        mid=(l+r)>>1
        if(L<=mid):
            update(rt<<1,l,mid,L,R,k)
        if(R>mid):
            update(rt<<1|1,mid+1,r,L,R,k)
        a[rt]=(a[rt<<1]+a[rt<<1|1])%Mod
###线段树

def qRange(x,y):
    global n,res,Mod
    ans=0
    while(top[x]!=top[y]):
        if(dep[top[x]]<dep[top[y]]):
            x,y=y,x
        res=0
        query(1,1,n,idd[top[x]],idd[x])
        ans+=res
        ans%=Mod
        x=fa[top[x]]
    if(dep[x]>dep[y]):
        x,y=y,x
    res=0
    query(1,1,n,idd[x],idd[y])
    ans+=res
    return ans%Mod
def updRange(x,y,k):
    global Mod
    k%=Mod
    while(top[x]!=top[y]):
        if(dep[top[x]]<dep[top[y]]):
            x,y=y,x
        update(1,1,n,idd[top[x]],idd[x],k)
        x=fa[top[x]]
    if(dep[x]>dep[y]):
        x,y=y,x
    update(1,1,n,idd[x],idd[y],k)
def qSon(x):
    global res
    res=0
    query(1,1,n,idd[x],idd[x]+siz[x]-1)
    return res
def updSon(x,k):
    update(1,1,n,idd[x],idd[x]+siz[x]-1,k)
def dfs1(x,f,deep):
    dep[x],fa[x],siz[x]=deep,f,1
    maxson,i=-1,beg[x]
    while(i):
        y=to[i]
        if(y==f):
            i=nex[i]
            continue
        dfs1(y,x,deep+1)
        siz[x]+=siz[y]
        if(siz[y]>maxson):
            son[x],maxson=y,siz[y]
        i=nex[i]
def dfs2(x,topf):
    global cnt
    cnt+=1
    idd[x]=cnt
    wt[cnt],top[x]=w[x],topf
    if(not son[x]):
        return
    dfs2(son[x],topf)
    i=beg[x]
    while(i):
        y=to[i]
        if(y==fa[x] or y==son[x]):
            i=nex[i]
            continue
        dfs2(y,y)
        i=nex[i]


n,m,r,Mod=map(int,input().split())
N=n+5
e,beg,nex,to,w,wt=0,[0]*N,[0]*N,[0]*N,[0]*N,[0]*N
a,laz,res=[0]*(N<<2),[0]*(N<<2),0
son,idd,fa,dep,siz,top,cnt=[0]*N,[0]*N,[0]*N,[0]*N,[0]*N,[0]*N,0

w[1:n+1]=map(int,input().split())
for i in range(n-1):
    u,v=map(int,input().split())
    addedge(u,v)
    addedge(v,u)
dfs1(r,0,1)
dfs2(r,r)
build(1,1,n)
for _ in range(m):
    act=list(map(int,input().split()))
    if(act[0]==1):
        x,y,z=act[1:4]
        updRange(x,y,z)
    elif(act[0]==2):
        x,y=act[1:3]
        print(qRange(x,y))
    elif(act[0]==3):
        x,y=act[1:3]
        updSon(x,y)
    else:
        x=act[1]
        print(qSon(x))