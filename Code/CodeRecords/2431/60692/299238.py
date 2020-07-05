import math
from collections import defaultdict
x, y, edges = [0], [0], [[]]
fa = defaultdict(int)
s_p = input().split(" ")
s = int(s_p[0])
p = int(s_p[1])


def dis(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))


def findfa(z: int):
    if z == fa[z]:
        return z
    return findfa(fa[z])


def krustal():
    edges.sort()
    count, ans = 0, 0
    for i in range(1, p + 1):
        u = findfa(edges[i][1])
        v = findfa(edges[i][2])
        if u == v:
            continue
        else:
            fa[u] = v
            ans = edges[i][0]
            count += 1
            if count >= p - s:
                break
    return ans


for i in range(1, p + 1):
    fa[i] = i
    x_y = input().split(" ")
    x.append(int(x_y[0]))
    y.append(int(x_y[1]))
    for j in range(1, i):
        d = dis(x[i], y[i], x[j], y[j])
        edges.append([d, i, j])

print(round(krustal(), 2))

