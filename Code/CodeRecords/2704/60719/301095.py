def find(x, p):
    if x == p[x]:
        return x
    else:
        p[x] = find(p[x], p)
        return p[x]


def findconnection(tree):
    if not tree:
        return []
    n = len(tree)
    parent = [i for i in range(n+1)]
    for edge in tree:
        p = find(edge[0], parent)
        q = find(edge[1], parent)
        if p == q:
            return edge
        parent[p] = q
    return []


tree = eval(input())
res = findconnection(tree)
print(res)