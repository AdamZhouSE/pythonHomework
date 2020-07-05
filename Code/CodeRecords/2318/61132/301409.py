def seartree(l,u):
    if not l[u]:
        print("impossible")
        return 1
    le=ri=0
    if l[u][0]>=0:
        if l[u][0]>=u:
            return -1
        else:
            le=seartree(l,l[u][0])
    if l[u][1]>=0:
        if l[u][1]<=u:
            return -1
        else:
            ri=seartree(l,l[u][1])
    return 1+le+ri if le>=0 and ri>=0 else -1

def dfs3(l,u):
    tmp=seartree(l,u)
    if tmp>=0:return tmp
    le=ri=0
    if l[u][0]>=0:
        le=dfs3(l,l[u][0])
    if l[u][0]>=0:
        ri=dfs3(l,l[u][1])
    return max(le,ri,1)

# t=int(input())
t,root=map(int,input().split())
g = [[] for i in range(t)]
for j in range(t):
    u,l,r= map(int, input().split())
    g[u - 1]+=[l-1,r-1]
print(dfs3(g,root-1))