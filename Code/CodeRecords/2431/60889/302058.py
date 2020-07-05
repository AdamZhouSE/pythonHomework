import math

PS=input().split(" ")
P = int(PS[0])
S = int(PS[1])
distances = []
points = []
for i in range(S):
    point = list(map(int,input().split(" ")))
    points.append(point)
for i in points:
    distance = []
    for j in points:
        distance.append(math.sqrt((j[0]-i[0])**2+(j[1]-i[1])**2))
    distances.append(distance)
for i in range(S-P):
    minD = distances[0][1]+1
    minM = 0
    minN = 0
    for m in range(S-i):
        for n in range(S-i):
            if distances[m][n] < minD and distances[m][n] != 0:
                minD = distances[m][n]
                minM = m
                minN = n
    for j in range(S-i):
        if distances[minM][j]>distances[minN][j]:
            distances[minM][j]=distances[minN][j]
            distances[j][minM]=distances[j][minN]
    del distances[minN]
    for j in distances:
        del j[minN]
print(format(minD,".2f"),end="")
            
            
            