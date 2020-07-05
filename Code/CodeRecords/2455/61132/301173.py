def dfs1(l,tr,vi,u):
    Sum=0
    for i in l[u]:
        if vi[i]==0:
            vi[u]=1
            Sum+=dfs1(l,tr,vi,i)
            vi[u]=0
    return max(0,Sum+tr[u])

t=int(input())
g = [[] for i in range(t)]
vi=[0 for i in range(t)]
tr=list(map(int,input().split()))
for j in range(t - 1):
    u, v= map(int, input().split())
    g[u - 1].append(v-1)
    g[v - 1].append(u-1)
Max=0
for i in range(t):
    Max=max(Max,dfs1(g,tr,vi,i))
print(Max)