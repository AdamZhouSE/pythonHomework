import math
maxSize = 0.0000
n = int(input())
liOfPoints = []
for i in range(n):
    liOfPoints.append(list(eval("["+input()+"]")))
edges = []
# [from, to, lenSquare, center]
for i in range(n):
    for j in range(i+1, n):
        center = [(liOfPoints[i][0] + liOfPoints[j][0])/2, (liOfPoints[i][1] + liOfPoints[j][1])/2]
        lenSquare = pow((liOfPoints[i][0] - liOfPoints[j][0]), 2) + pow((liOfPoints[i][1] - liOfPoints[j][1]), 2)
        edges.append([liOfPoints[i], liOfPoints[j], lenSquare, center])

for i in range(len(edges)):
    for j in range(i+1, len(edges)):
        line1 = edges[i]
        line2 = edges[j]
        if line1[2] != line2[2] or line1[3] != line2[3]:
            continue
        sq1 = pow((line1[0][0] - line2[0][0]), 2) + pow((line1[0][1] - line2[0][1]), 2)
        sq2 = pow((line1[0][0] - line2[1][0]), 2) + pow((line1[0][1] - line2[1][1]), 2)
        maxSize = max(maxSize, sq1*sq2)

print(math.sqrt(maxSize))