def isCrossing(lineOne,lineTwo):
    x1 = lineOne[0]
    y1 = lineOne[1]
    x2 = lineOne[2]
    y2 = lineOne[3]
    x3 = lineTwo[0]
    y3 = lineTwo[1]
    x4 = lineTwo[2]
    y4 = lineTwo[3]
    if(((x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)) * ((x2 - x1) * (y4 - y1) - (y2 - y1) * (x4 - x1)) <= 0):
        return False
    else:
        return True

t = int(input())
for i in range(0,t):
    pointOne = list(map(int,input().split(' ')))
    pointTwo = list(map(int,input().split(' ')))
    pointThree = list(map(int,input().split(' ')))
    EdgeOne = pointOne + pointTwo
    EdgeTwo = pointTwo + pointThree
    EdgeThree = pointOne + pointThree
    minX = min([pointOne[0],pointTwo[0],pointThree[0]])
    maxX = max([pointOne[0],pointTwo[0],pointThree[0]])
    minY = min([pointOne[1],pointTwo[1],pointThree[1]])
    maxY = max([pointOne[1],pointTwo[1],pointThree[1]])
    count = 0
    for x in range(minX + 1,maxX):
        for y in range(minY + 1,maxY):
            if(isCrossing(EdgeOne,[x,y] + pointThree) and isCrossing(EdgeTwo,[x,y] + pointOne) and isCrossing(EdgeThree,[x,y] + pointTwo)):
                count = count + 1
    print(count)