def find(points):
    res = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[j][0]
            y2 = points[j][1]
            if (abs(x2 - x1) + abs(y2 - y1))**2 == ((x2 - x1) ** 2 + (y2 - y1) ** 2) and (x1!=x2 or y1!=y2):
                res += 1
    return res


t = int(input())
for i in range(t):
    n = int(input())
    points = []
    for _ in range(n):
        points.append([int(i) for i in input().split(" ")])
    print(find(points))
