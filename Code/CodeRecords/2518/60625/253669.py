def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count


housesPositionList=input().split(',')
heaterPositionList=input().split(',')
heaterPosition=[]
housesPosition=[]
for position in housesPositionList:
    housesPosition.append(int(position))
for position in heaterPositionList:
    heaterPosition.append(int(position))
range=0
check=0
rangeList = []
while check==0:
    check=1
    for position in heaterPosition:
        rangeList.append(position-range)
        rangeList.append(position + range)
    rangeList=list(set(rangeList))

    for position in housesPosition:
        if countX(rangeList,position)==0:
            check=0
            range+=1
            break
print(range)
