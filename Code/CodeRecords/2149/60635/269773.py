info = input().split()
n = int(info[0])
k = int(info[1])
tree=[[0 for i in range(n+1)]for j in range(n+1)]
size=[0 for i in range(n+1)]
def link(u,v):
    tree[u][v]=1
    tree[v][u]=1
def cut(u,v):
    tree[u][v]=0
    tree[v][u]=0
for i in range(n-1):
    info = input().split()
    u = int(info[0])
    v = int(info[1])
    link(u,v)
def getgravity(i,f):
    size[i]=1
    gravity=-1
    isg=True
    for j in range(1,n+1):
        if tree[i][j]>0 and j!=f:
            x=getgravity(j,i)
            if x>-1:gravity=x
            size[i]+=size[j]
            if size[j]>n/2:
                isg=False
    if n-size[i]>n/2:
        isg=False
    if isg:
        gravity=i
    return gravity
id=[0 for i in range(n+1)]
rt=[0 for i in range(n+1)]
lis=[0 for i in range(n+1)]
rk=[0 for i in range(n+1)]
ssum=[0 for i in range(n+1)]
cnt=0
def fil(i,f,x):
    id[i]=x
    for j in range(1,n+1):
        if tree[i][j]>0 and j!=f:
            fil(j,i,x)
def check(i):
    if i==gravity or cnt<=k:
        return 1
    s=ssum[cnt-k]+1
    if rk[id[i]]>=cnt-k:
        t=ssum[cnt - k - 1] + size[rt[id[i]]] - size[i] + 1
        s=min(t,s)
    else:
        s-=size[i]
    return int(s<=n/2)
gravity=getgravity(1,0)
getgravity(gravity,0)
for i in range(1,n+1):
    if tree[gravity][i]>0:
        fil(i,gravity,cnt)
        lis[cnt]=cnt
        rt[cnt]=i
        cnt+=1
lis=lis[:cnt]
lis.sort(key=lambda x:size[rt[x]])
for i in range(cnt):
    rk[lis[i]]=i
    ssum[i + 1] = ssum[i] + size[rt[lis[i]]]
for i in range(1,n+1):
    print(check(i))
