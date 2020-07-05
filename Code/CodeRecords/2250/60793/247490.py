class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


def maxPoints(apoints):
    size = len(apoints)
    if size in [0,1]:
        return size
    res = 0
    for i in range(size):
        cur_max = 1
        d = {}
        count = 0
        dup = 0
        for j in range(size):
            if j!=i:
                deta_x = apoints[i].x - apoints[j].x
                deta_y = apoints[i].y - apoints[j].y
                if deta_x == 0 and deta_y == 0:
                    dup += 1
                elif deta_x == 0:
                    if count == 0:
                        count = 2
                    else:
                        count += 1
                    cur_max = max(count,cur_max)
                else:
                    k = deta_y/deta_x
                    if d.get(k) == None:
                        d[k] = 2
                    else:
                        d[k] += 1
                    cur_max = max(d[k],cur_max)
        res = max(res,cur_max + dup)
    return res


point_num = int(input())
points = []
result = True
for i in range(0, point_num):
    temp = list(map(int, input().split(",")))
    points.append(Point(temp[0], temp[1]))
print(maxPoints(points))