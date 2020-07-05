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