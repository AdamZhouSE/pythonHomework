num_of_ponits=int(input())
pointsList=[]
pointStr=[]
for i in range(num_of_ponits):
    point=[]
    pointStr=input().split(',')
    for position in pointStr:
        point.append(int(position))
    pointsList.append(point)


def maxPoints(pointsList):
    if len(pointsList)==0:
        return 0
    if len(pointsList)<=2:
        return len(pointsList)
    max=2
    for m in range(len(pointsList)):
        samePosition=0
        sameSlope=1
        for n in range(m+1,len(pointsList)):
            positionX = pointsList[n][0]-pointsList[m][0]
            positionY = pointsList[n][1] - pointsList[m][1]
            if positionX==0 and positionY==0:
                samePosition+=1
            else:
                sameSlope+=1
                for k in range(n+1,len(pointsList)):
                    positionX2 = pointsList[k][0] - pointsList[m][0]
                    positionY2 = pointsList[k][1] - pointsList[m][1]
                    if positionX*positionY2==positionY*positionX2:
                        sameSlope+=1
            if max < samePosition+sameSlope:
                max = samePosition + sameSlope
            sameSlope=1
    return max


print(maxPoints(pointsList))