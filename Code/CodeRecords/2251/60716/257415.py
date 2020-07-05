n = int(input())
points = list()
for i in range(n):
    strs = input().split(',')
    local = [int(j) for j in strs]
    points.append(local)
area = 0
for i in range(len(points)-2):
    for k in range(i+1, len(points)-1):
        for m in range(k+1, len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[k][0]
            y2 = points[k][1]
            x3 = points[m][0]
            y3 = points[m][1]
            area = max(area, abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3)))
print(area/2)