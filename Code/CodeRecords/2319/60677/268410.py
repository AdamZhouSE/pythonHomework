def getNear(doubleList,x,y):
    XY=[]
    if x+1<doubleList.__len__():
        XY.append([x+1,y])
    if x-1>=0:
        XY.append([x-1,y])
    if y+1<doubleList[0].__len__():
        XY.append([x,y+1])
    if y-1>=0:
        XY.append([x,y-1])

    return XY
def getSquare(doubleList,x,y,near):
    square=0
    if doubleList[near[0]][near[1]]<doubleList[x][y]:
        square=doubleList[near[0]][near[1]]
    else:
        square=doubleList[x][y]
    return square
def getTowerSquare(n):
    if n==0:
        return 0
    else:
        return 4*n+2
def getSurfaceArea():
    n=int(input())
    doubleList=[]
    for i in range(n):
        line=input().split(',')
        doubleList.append([int(x) for x in line])
    square = 0
    for i in range(doubleList.__len__()):
        for j in range(doubleList[i].__len__()):
            square += getTowerSquare(doubleList[i][j])
            nearList=getNear(doubleList,i,j)
            for near in nearList:
                square-=getSquare(doubleList,i,j,near)
    return square
print(getSurfaceArea())