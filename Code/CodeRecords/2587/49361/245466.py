def calculator(point1, point2):
    x0 = point1[1]
    y0 = point1[0]
    x1 = point2[1]
    y1 = point2[0]
    return max(abs(y1 - y0), abs(x1 - x0))


points = []
numOfPoints = int(input())
for i in range(numOfPoints):
    s = input()
    x = int(s.split(",")[0])
    y = int(s.split(",")[1])
    points.append([x, y])
time = 0
for i, point in enumerate(points):
    if i > 0:
        time += calculator(point, points[i - 1])

print(time)
