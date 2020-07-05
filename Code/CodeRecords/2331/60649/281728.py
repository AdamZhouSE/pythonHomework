n,m,k=map(int,input().split())
k=n-k+1
lim=-1
mp=[[0 for i in range(m+1)]for j in range(n+1)]
vis=[0 for i in range(255)]
lin=vis.copy()
tot=5
def dfs(u,lim):
    global vis,lin,tot
    for i in range(1,m+1):
        if mp[u][i]<=lim and vis[i]!=tot:
            vis[i]=tot
            if lin[i] == 0 or dfs(lin[i], lim) == 1:
                lin[i] = u
                return 1
    return 0
def check(x):
    global tot,vis,lin
    vis=[0 for i in range(255)]
    lin=vis.copy()
    tot,ans=1,0
    for i in range(1,n+1):
        ans+=dfs(i,x)
        tot+=1
    return ans
for i in range(1,n+1):
    l=list(map(int,input().split()))
    for j in range(1,m+1):
        mp[i][j]=l[j-1]
        lim=max(lim,l[j-1])
l,r=1,lim
while l<r:
    mid=(l+r)//2
    if check(mid)>=k:
        r=mid
    else:
        l=mid+1
print(l)


