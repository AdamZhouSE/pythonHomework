from collections import defaultdict
edges = [[]]
fa = defaultdict(int)
n_k = input().split(" ")
n = int(n_k[0])
k = int(n_k[1])
sum = 0
for i in range(k):
    u_v_w = input().split(" ")
    u = int(u_v_w[0])
    v = int(u_v_w[1])
    w = int(u_v_w[2])
    edges.append([w, u, v])
    sum += w


def findfa(x: int):
    if x == fa[x]:
        return x
    return findfa(fa[x])


def krustal():
    res = 0
    edges.sort()
    for a in range(1, n + 1):
        fa[a] = a
    for j in range(1, k + 1):
        x = findfa(edges[j][1])
        y = findfa(edges[j][2])
        if x == y:
            continue
        else:
            fa[x] = y
            res += edges[j][0]
    return res


print(sum - krustal())