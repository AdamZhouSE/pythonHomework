def maxPoints(points):
    size = len(points)
    if size in [0, 1]:
        return size
    res = 0
    for i in range(size):
        cur_max = 1
        d = {}
        count = 0
        dup = 0
        for j in range(size):
            if j != i:
                deta_x = points[i][0] - points[j][0]
                deta_y = points[i][1] - points[j][1]
                if deta_x == 0 and deta_y == 0:
                    dup += 1
                elif deta_x == 0:
                    if count == 0:
                        count = 2
                    else:
                        count += 1
                    cur_max = max(count, cur_max)
                else:
                    k = deta_y / deta_x
                    if d.get(k) == None:
                        d[k] = 2
                    else:
                        d[k] += 1
                    cur_max = max(d[k], cur_max)
        res = max(res, cur_max + dup)
    return res

points = []
N = eval(input())
for i in range(N):
    points.append(list(map(int,input().split(','))))
print(maxPoints(points))