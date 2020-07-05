n = int(input())
points = []
res = 0
for i in range(n):
    points.append([int(i) for i in input().split(",")])
for i in range(n-1):
    x = abs(points[i][0] - points[i+1][0])
    y = abs(points[i][1] - points[i+1][1])
    res += min(x,y)
    res += max(x,y) - min(x,y)
print(res)