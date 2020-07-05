def dfs2(l,u):
    if not l:return True
    le=ri=True
    if l[u][0]>=0:
        if l[u][0]>=u:
            return False
        else:
            le=dfs2(l,l[u][0])
    if l[u][1]>=0:
        if l[u][1]<=u:
            return False
        else:
            ri=dfs2(l,l[u][1])
    return le and ri

def comtree(l,u):
    q = [u]
    while True:
        if q:
            tmp = q.pop(0)
        else:
            return True
        for i in l[u]:
            if q[-1] == -1 and i!=-1:
                return False
            q.append(i)

t,u=map(int,input().split())
g = [[] for i in range(t)]
for j in range(t - 1):
    u,l,r= map(int, input().split())
    g[u - 1]+=[l-1,r-1]
print(dfs2(g,u))
print(comtree(g,u))