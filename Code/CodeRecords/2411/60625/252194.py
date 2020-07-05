num_point=int(input())
coodinates=[]
for i in range(num_point):
    point=input().split(',')
    coodinates.append(point)
Old_xDistance=int(coodinates[0][0])-int(coodinates[1][0])
Old_yDistance=int(coodinates[0][1]) - int(coodinates[1][1])

check=1
for pointIndex in range(len(coodinates)-1):
    xDistance = int(coodinates[pointIndex][0])-int(coodinates[pointIndex+1][0])
    yDistance = int(coodinates[pointIndex][1]) - int(coodinates[pointIndex + 1][1])
    if Old_xDistance!=xDistance or Old_yDistance!=yDistance:
        check=0
        print(False)
        break
if check==1:
    print(True)