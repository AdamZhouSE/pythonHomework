def dfs2(l,u):
    if not l[u]:return True
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
        tmp = q.pop(0)
        if tmp == -1:
            return True
        for i in l[tmp]:
            if q and q[-1] == -1 and i!=-1:
                return False
            q.append(i)

t,root=map(int,input().split())
g = [[] for i in range(100)]
for j in range(t):
    u,l,r= map(int, input().split())
    g[u - 1]+=[l-1,r-1]
print('true' if dfs2(g,root-1) else 'false')
print('true' if comtree(g,root-1) else 'false')