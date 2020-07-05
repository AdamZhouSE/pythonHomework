import math
import collections
num=int(input())
points=[]
for i in range(num):
    po=input().split(",")
    po=list(map(int,po))
    points.append(po)

N = len(points)
d = collections.defaultdict(list)
for i in range(N - 1):
    pi = points[i]
    for j in range(i + 1, N):
        pj = points[j]
        l = (pi[0] - pj[0]) ** 2 + (pi[1] - pj[1]) ** 2
        x = (pi[0] + pj[0]) / 2.0
        y = (pi[1] + pj[1]) / 2.0
        d[(l, x, y)].append((i, j))
res = float("inf")
for l in d.values():
    M = len(l)
    for i in range(M - 1):
        p0, p2 = points[l[i][0]], points[l[i][1]]
        for j in range(i + 1, M):
            p1, p3 = points[l[j][0]], points[l[j][1]]
            d1 = math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)
            d2 = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
            area = d1 * d2
            res = min(res, area)
if res == float('inf'):
    print("0.0000")
else:
    print(format(res,'.4f'))
