N=50005
tot,sum,ans,top,col=1,0,0,0,0
def memset(sources):
    res=[]
    for i in range(N):
        res.append(sources)
    return res
ne=memset(0)
la=memset(0)
lnk=memset(0)
dfn=memset(0)
low=memset(0)
st=memset(0)
num=memset(0)
vis=memset(0)
du=memset(0)
def add(x,y):
    global tot
    tot+=1
    ne[tot]=y
    la[tot]=lnk[x]
    lnk[x]=tot
def dfs(u):
    global sum,top,col
    sum+=1
    low[u]=dfn[u]=sum
    top+=1
    st[top]=u
    k=lnk[u]
    while(k):
        vis[k]=1
        if not vis[k^1]:
            v=ne[k]
            if not dfn[v]:
                dfs[v]
                low[u]=min(low[u],low[v])
            else:
                low[u]=min(low[u],dfn[v])
        k=la[k]
    if dfn[u]==low[u]:
        col+=1
        num[u]=col
        while st[top]!=u:
            num[st[top]]=col
            top-=1
        top-=1
n_m=input().split(" ")
n=int(n_m[0])
m=int(n_m[1])
for i in range(1,m+1):
    x_y=input().split(" ")
    x=int(x_y[0])
    y=int(x_y[1])
    add(x,y)
    add(y,x)
dfs(1)
for i in range(n+1):
    j=lnk[i]
    while(j):
        vis[j]=0
        if vis[j^1]:
            if num[i]!=num[ne[j]]:
                du[num[i]]+=1
                du[num[ne[j]]]+=1
        j=la[j]
for i in range(1,col+1):
    if du[i]==1:
        ans+=1
print(int((ans+1)/2),end="")
    


























































