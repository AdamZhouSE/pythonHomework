r = int(input())
c = int(input())
r0 = int(input())
c0 = int(input())
totSize = r*c
currentPoint = [r0, c0]
path = [currentPoint.copy()]
cntStep = 0
while len(path) < totSize:
    # if cntStep == 20: break
    # print(currentPoint)
    direction = cntStep % 4
    pathStep = cntStep // 2 + 1
    if direction == 0:
        for i in range(pathStep):
            currentPoint[1] += 1
            if 0 <= currentPoint[1] < c and 0 <= currentPoint[0] < r:
                path.append(currentPoint.copy())
    elif direction == 1:
        for i in range(pathStep):
            currentPoint[0] += 1
            if 0 <= currentPoint[1] < c and 0 <= currentPoint[0] < r:
                path.append(currentPoint.copy())
    elif direction == 2:
        for i in range(pathStep):
            currentPoint[1] -= 1
            if 0 <= currentPoint[1] < c and 0 <= currentPoint[0] < r:
                path.append(currentPoint.copy())
    elif direction == 3:
        for i in range(pathStep):
            currentPoint[0] -= 1
            if 0 <= currentPoint[1] < c and 0 <= currentPoint[0] < r:
                path.append(currentPoint.copy())
    cntStep += 1

print(path)