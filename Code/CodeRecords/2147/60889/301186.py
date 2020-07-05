def findBeatWay(loc,roads):
    hasReach = []
    minLengths = []
    leftPlace = len(roads)-1
    for i in range(len(roads)):
        if i == loc:
            hasReach.append(1)
            minLengths.append(0)
        else:
            hasReach.append(0)
            minLengths.append(-1)
    while leftPlace != 0:
        leftPlace = leftPlace - 1
        nextPoint = -1
        minLength = 0
        for i in range(len(roads)):
            if hasReach[i] == 1:
                continue
            if roads[loc][i] != -1:
                length = minLengths[loc] + roads[loc][i]
                if (minLengths[i] == -1) or (minLengths[i] > length):
                    minLengths[i] = length
            if (nextPoint == -1) and (roads[loc][i] != -1):
                nextPoint = i
                minLength = minLengths[i]
            elif (minLength > minLengths[i]) and (roads[loc][i] != -1):
                nextPoint = i
                minLength = minLengths[i]
        hasReach[nextPoint] = 1
        loc = nextPoint
    return minLengths

NMKAB = input().split(" ")
n = int(NMKAB[0])
m = int(NMKAB[1])
k = int(NMKAB[2])
a = int(NMKAB[3])
b = int(NMKAB[4])
roads = []
for i in range(n):
    road = []
    for j in range(n):
        if i == j:
            road.append(0)
        else:
            road.append(-1)
    roads.append(road)
for i in range(m):
    road = input().split(" ")
    c = int(road[0])-1
    d = int(road[1])-1
    roads[c][d] = a
    roads[d][c] = a
for l in range(n):
    for i in range(n):
        for j in range(n):
            if (roads[i][l] == roads[l][j] == a) and (roads[i][j] != a) and (i != j):
                roads[i][j] = b
ways = findBeatWay(k-1,roads)
for i in ways:
    print(i)
    
    
    
    
    
    
    
    
    
