def todan(l,u,f):
    obj=[]
    for i in l[u]:
        if i[0]==f:
            obj=i
        else:
            todan(l,i[0],u)
    if obj:
        l[u].remove(obj)

def dfs(l,u,k):
    if len(l[u])==0 or k==0:
        return 0
    elif len(l[u])==1:
        return l[u][0][1]+dfs(l,l[u][0][0],k-1)
    else:
        if k==1:
            return max(l[u][0][1],l[u][1][1])
        else:
            Max = max(l[u][0][1] + dfs(l, l[u][0][0], k - 1), l[u][1][1] + dfs(l, l[u][1][0], k - 1))
            for i in range(1, k):
                Max = max(Max, l[u][0][1] + dfs(l, l[u][0][0],i-1) + l[u][1][1] + dfs(l, l[u][1][0],k-i-1))
            return Max

t,k = map(int,input().split())
g=[[] for i in range(t)]
for j in range(t-1):
    u,v,val=map(int,input().split())
    g[u-1].append([v-1,val])
    g[v-1].append([u-1,val])
todan(g,0,-1)
print(dfs(g,0,k))