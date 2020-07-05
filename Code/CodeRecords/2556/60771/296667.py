#20
from itertools import combinations

ori = input().split(" ")
N = int(ori[0])
K = int(ori[1])
points = []
for i in range(0,N):
    ori = input().split(" ")
    xy = [int(item) for item in ori]
    points.append(xy)

points.sort()
res = []
l = list(combinations(points,2))
for item in l:
    x1 = item[0][0]
    y1 = item[0][1]
    x2 = item[1][0]
    y2 = item[1][1]

    if abs(x1-x2)>=K or abs(y1-y2)>=K:
        continue
    if y2 <= y1:
        x1 += K//2
        y1 -= K//2
        x2 -= K//2
        y2 += K//2
        res.append(abs((x1-x2)*(y1-y2)))
    else:
        x1 += K//2
        y1 += K//2
        x2 -= K//2
        y2 -= K//2
        res.append(abs((x1-x2)*(y1-y2)))

if len(res) == 1:
    print(res[0])
elif len(res) == 0:
    print(0)
else:
    print(-1)

