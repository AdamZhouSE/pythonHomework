def dfs(l,vi,u):
    ans=[]
    for i in l[u]:
        if vi[i]==0:
            vi[i]=1
            ans.append(dfs(l,vi,i))
            vi[i]=0
    return 1+max(ans) if ans else 0

t = int(input())
g=[[] for i in range(t)]
vi=[0 for i in range(t)]
for j in range(t-1):
    u,v=map(int,input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)
Max=0
for i in range(len(g)):
    if len(g[i])==1:
        Max=max(Max,dfs(g,vi,i))
print(Max)