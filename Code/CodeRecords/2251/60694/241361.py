# S=(1/2) * abs(x1y2 + x2y3 + x3y1 - x1y3 - x2y1 - x3y2)
n = int(input())
points = []
for i in range(n):
    point = []
    x, y = map(int, input().split(","))
    point.append(x)
    point.append(y)
    points.append(point)

maxArea = 0.0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            tmp = abs(points[i][0] * points[j][1] + points[j][0] * points[k][1] +
                      points[k][0] * points[i][1] - points[i][0] * points[k][1] -
                      points[j][0] * points[i][1] - points[k][0] * points[j][1]) / 2
            maxArea = max(tmp, maxArea)

print(maxArea)

