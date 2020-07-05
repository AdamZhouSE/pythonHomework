n=int(input())
coordinates=[]
for i in range(0,n):
    tmp=list(map(int,input().split(',')))
    coordinates.append(tmp)
k=(coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
oneline=True
for i in range(2,n):
    if (coordinates[i][1]-coordinates[0][1])/(coordinates[i][0]-coordinates[0][0])!=k:
        oneline=False
        break
print(oneline)