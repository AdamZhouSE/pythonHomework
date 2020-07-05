def getKandD(pointA, pointB):
    k =(pointA[1] - pointB[1]) / (pointA[0] - pointB[0])
    b = pointA[1] - k * pointA[0]
    return [k, b]


nums = int(input())
coordinates = []
for i in range(0, nums):
    row = input().split(',')
    row[0] = int(row[0])
    row[1] = int(row[1])
    coordinates.append(row)
lines = []
points = []
for i in range(0, len(coordinates) - 1):
    for j in range(i + 1, len(coordinates)):
        kANDd = getKandD(coordinates[i], coordinates[j])
        if lines.count(kANDd) == 0:
            lines.append(kANDd)
            points.append([coordinates[i], coordinates[j]])
        else:
            index = lines.index(kANDd)
            points[index] += [coordinates[i], coordinates[j]]

for i in range(0, len(points)):
    #     i是每一条直线的点的数组  i:[     [1, 1], [2, 2], [1, 1], [3, 3], [2, 2], [3, 3]      ]
    indexOuter = 0
    while indexOuter < len(points[i]):
        tempCMP = points[i][indexOuter]
        indexInner = indexOuter + 1
        while indexInner < len(points[i]):
            if points[i][indexInner] == tempCMP:
                del points[i][indexInner]
                indexInner -= 1
            indexInner += 1
        indexOuter += 1
    points[i] = len(points[i])
points.sort(reverse=True)
print(points[0])