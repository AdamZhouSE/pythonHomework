import numpy as np

points = []
sz = eval(input())
for i in range(sz):
    points.append([int(x) for x in input().split(',')])
curMaxArea = 0
# sz = len(points)
for i in range(sz):
    for j in range(i + 1, sz):
        for k in range(j + 1, sz):
            arr = np.array([[points[i][0], points[i][1], 1],
                            [points[j][0], points[j][1], 1],
                            [points[k][0], points[k][1], 1]
                            ])
            tempArea = abs(np.linalg.det(arr)) / 2
            if tempArea > curMaxArea:
                curMaxArea = tempArea
print(curMaxArea)