numberOfStation=int(input())
distancesList=input().split()
distances=[]
for c in distancesList:
    distances.append(int(c))

stationList=input().split()
stationList.sort()
stationA=int(stationList[0])
stationB=int(stationList[1])

clock=0
anticlockwise=0

for index in range(stationA-1,stationB-1):
    clock+=distances[index]
for index in range(stationB-1,numberOfStation):
    anticlockwise+=distances[index]
if clock>=anticlockwise:
    print(anticlockwise)
else:
    print(clock)