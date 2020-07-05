points = eval(input())
k = int(input())
for i in range(0, len(points)):
    points[i].append(pow(points[i][0], 2) + pow(points[i][1], 2))
points.sort(key=lambda x: x[2])
print([x[: -1] for x in points[0: k]])
