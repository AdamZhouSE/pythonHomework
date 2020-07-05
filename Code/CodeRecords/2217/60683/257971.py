def cmpPoint(p1, p2):
    if p1[0] > p2[0]:
        return 1
    elif p1[0] == p2[0] and p1[1] > p2[0]:
        return 1
    return -1


points = []
for i in range(4):
    temp = [int(x) for x in input().split(',')]
    points.append(temp)
from functools import cmp_to_key

points = sorted(points, key=cmp_to_key(cmpPoint))

# print(points)
res = []
for i in range(0, 4, 2):
    temp1 = points[i+1][0] - points[i][0]
    temp2 = points[i+1][1] - points[i][1]
    res.append([temp1,temp2])
# print(res)
if res[0] == res[1]:
    print(True)
else:
    print(False)