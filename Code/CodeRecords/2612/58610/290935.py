from math import sqrt

def distant(point1, point2):
    dist1 = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    dist2 = int(sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2))
    return 1 if dist1 == dist2 else 0

points = [list(map(int, input().split(' '))) for i in range(eval(input()))]
total = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        total += distant(points[i], points[j])
print(total)