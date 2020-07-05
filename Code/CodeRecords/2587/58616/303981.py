# LeetCode 1266
def minTimeToVisitAllPoints(points):
    x0, x1 = points[0]
    ans = 0
    for i in range(1, len(points)):
        y0, y1 = points[i]
        ans += max(abs(x0 - y0), abs(x1 - y1))
        x0, x1 = points[i]
    return ans


pointCount = eval(input())
points = []
for count in range(pointCount):
    xAndy = input().split(',')
    x = eval(xAndy[0])
    y = eval(xAndy[1])
    points.append([x, y])
print(minTimeToVisitAllPoints(points))