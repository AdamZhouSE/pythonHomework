def cross(p1, p2, p3):
    x1 = p2[0] - p1[0]
    x2 = p3[0] - p1[0]
    y1 = p2[1] - p1[1]
    y2 = p3[1] - p1[1]
    return x1 * y2 - x2 * y1


n = int(input())
res = []
for i in range(n):
    points = []
    for j in range(2):
        line = list(map(int, input().split()))
        points.append(line)
    a = [points[0][0], points[0][1]]
    b = [points[0][2], points[0][3]]
    c = [points[1][0], points[1][1]]
    d = [points[1][2], points[1][3]]
    if min(a[0], b[0]) < max(c[0], d[0]) and min(c[1], d[1]) < max(a[1], b[1]) and min(c[0], d[0]) <= max(a[0], b[
        0]) and min(a[1], b[1]) < max(c[1], d[1]):
        if cross(a, b, c) * cross(a, b, d) <= 0 and cross(c, d, a) * cross(c, d, b) <= 0:
            res.append(1)
        else:
            res.append(0)
    else:
        res.append(0)
for i in res:
    print(i)
    