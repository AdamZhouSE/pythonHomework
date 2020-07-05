import sys
import math
dl = lambda name: print(name, ':', sys._getframe().f_back.f_locals[name])
read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

n, m = read_line()
first = [-1] * n
next = [-1] * (2 * m)
dis = [1e18] * n
edges = []
for i in range(0, 2 * m, 2):
    a, b, c = read_line()
    edges.append((a - 1, b - 1, c))
    first[a - 1], next[i] = i, first[a - 1]
    edges.append((b - 1, a - 1, c))
    first[b - 1], next[i + 1] = i + 1, first[b - 1]

done = [0] * n
done[0] = 1
ei = first[0]
while ei is not -1:
    e = edges[ei]
    dis[e[1]] = min(dis[e[1]], e[2])
    ei=next[ei]
total = 0
for _ in range(n - 1):
    # print(done)
    # print(dis)
    # print(total)
    minv, mini = 1e20, -1
    for k, v in enumerate(dis):
        if not done[k] and v < minv:
            mini, minv = k, v
    done[mini] = 1
    total += minv
    e_index = first[mini]
    while e_index is not -1:
        e = edges[e_index]
        dis[e[1]] = min(dis[e[1]], e[2])
        e_index = next[e_index]

print(total if total < 1e16 else -1,end='')
