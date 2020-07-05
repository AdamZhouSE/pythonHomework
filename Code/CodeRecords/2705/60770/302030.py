# https://zhuanlan.zhihu.com/p/108302201

def solve():
    edges=eval(input())
    n=len(edges)
    degree=[0]*(n+1)
    for u,v in edges:
        degree[v]+=1
    for u,v in edges[::-1]:
        if degree[v]==2 and isWrong(edges,[u,v]):
            print([u,v])
            return
    print(isWrong(edges,[]))


def isWrong(edges,e):
    n=len(edges)
    roots=[i for i in range(n+1)]
    for u,v in edges:
        if [u,v]==e:
            continue
        if isSame(u,v,roots):
            return [u,v]
        join(u,v,roots)
    return []

def find(u,roots):
    if u==roots[u]:
        return u
    roots[u]=find(roots[u],roots)
    return roots[u]

def join(u,v,roots):
    u,v=find(u,roots),find(v,roots)
    if u==v:
        return
    roots[v]=u

def isSame(u,v,roots):
    u,v=find(u,roots),find(v,roots)
    return u==v

if __name__ == '__main__':
    solve()