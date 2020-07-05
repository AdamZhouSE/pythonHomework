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
        return True
    else:
        return False

t = int(input())
for i in range(0,t):
    lineOne = list(map(int,input().split(' ')))
    lineTwo = list(map(int,input().split(' ')))
    if(isCrossing(lineOne,lineTwo) and isCrossing(lineTwo,lineOne)):
        print(1)
    else:
        print(0)