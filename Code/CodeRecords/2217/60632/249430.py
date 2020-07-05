points = []
for i in range(4):
    points.append(list(map(int, input().split(','))))
points = sorted(points)
length = points[0][1] - points[1][1]
origin = points[0]
ideal = [origin, [origin[0], origin[1] + 1], [origin[0] + 1, origin[1]], [origin[0] + 1, origin[1] + 1]]
print(points == ideal)
