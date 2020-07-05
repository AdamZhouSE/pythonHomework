def dfs4(l, vi, u):
    Sum=0
    vi[u]=1
    for i in l[u]:
        if vi[i]==0:
            Sum += dfs4(l,vi,i)
    return Sum+1

def calnum(l, s):
    Max=0
    for i in range(len(l)):
        vi=[0 for i in l]
        vi[s]=1
        if i!=s:
            Max=max(Max, dfs4(l, vi, i))
    return Max

t=int(input())
g=[[] for i in range(t)]
for j in range(t-1):
    u, v= map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)
ans=[]
for i in range(t):
    ans.append(calnum(g,i))
Min=min(ans)
ans=[i+1 for i in range(len(ans)) if ans[i]==Min]
print(' '.join(map(str,ans)),end=' ')