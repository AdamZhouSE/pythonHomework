info=[int(x) for x in input().split()]
n,m=info[0],info[1]
graph=[[0]*n for i in range(n)]
edges=[[] for j in range(m)]
cur = 0


def add_edge(u,v,l):
    global cur
    edges[cur]=[u,v,l]
    cur += 1


fa={i:i for i in range(n)}


def find(x):
    if x!=fa[x]:
        fa[x]=find(fa[x])
    return fa[x]


def kruskal():
    edges.sort(key=lambda x:x[2])
    ans, cnt=0, 0
    for i in range(m):
        u=find(edges[i][0])
        v=find(edges[i][1])
        if u==v:
            continue
        ans+=edges[i][2]
        cnt+=1
        fa[v]=u
        if cnt==n-1:
            break
    return ans

for i in range(m):
    edge=[int(x) for x in input().split()]
    u=edge[0]-1
    v=edge[1]-1
    l=edge[2]
    add_edge(u,v,l)
print(kruskal(),end='')