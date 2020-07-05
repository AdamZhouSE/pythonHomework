def dpth(i):
    vis[i]=1
    for j in range(deg[i]):
        if(vis[a[i][j]]==0):
            dep[a[i][j]]=dep[i]+1
            dpth(a[i][j])

def dfs(i):
    for j in range(deg[i]):
        nxt=a[i][j]
        if(dep[nxt]>dep[i]):
            tmp=dfs(nxt)
            path[i]=max(path[i],tmp+1)
    return path[i]

def dia(i):
    left=-1
    right=-1
    Max=-1
    sMax=-1
    for j in range(deg[i]):
        nxt=a[i][j]
        if(dep[i]>dep[nxt]):
            dia(nxt)
            path[i]=max(path[i],path[nxt])
            if(Max<dep[nxt]): 
                left=nxt
                Max=dep[nxt]
    for j in range(deg[i]):
        nxt=a[i][j]
        if(dep[i]>dep[nxt] and nxt!=left):
            if(sMax<dep[nxt]): 
                right=nxt
                sMax=dep[nxt]
    if(left!=right and left!=-1 and right!=-1): path[i]=max(path[i],dep[left]+dep[right]+2)
            

n=int(input())
a=[[]*(n+1) for i in range(n+1)]
vis=[0]*(n+1)
dep=[0]*(n+1)
deg=[0]*(n+1)
for i in range(n-1):
    f,s=map(int,input().split())
    deg[f]+=1
    deg[s]+=1
    a[f].append(s)
    a[s].append(f)
dpth(1)
path=[0 for i in range(n+1)]
dfs(1)
dep=[path[i] for i in range(n+1)]
dia(1)
print(path[1])