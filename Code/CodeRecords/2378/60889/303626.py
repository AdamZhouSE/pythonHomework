def findShortest(roads):
    x=0
    y=0
    z=roads[0][0]
    for i in range(len(roads)):
        for j in range(len(roads)):
            if (roads[i][j] < z or z == 0) and roads[i][j] != 0:
                z = roads[i][j]
                x = i
                y = j
    for i in range(len(roads)):
        if ((roads[i][x] > roads[i][y] and roads[i][y]!=0) or (roads[i][x]==0)) and (i!=x):
            roads[i][x] = roads[i][y]
            roads[x][i] = roads[y][i]
    del roads[y]
    for i in roads:
        del i[y]
    return z

FR = input().split(" ")
numF = int(FR[0])
numR = int(FR[1])
roads = []
for i in range(numF):
    road = []
    for j in range(numF):
        road.append(0)
    roads.append(road)
rawLength = 0
for i in range(numR):
    road = input().split(" ")
    siteA = int(road[0])-1
    siteB = int(road[1])-1
    length = int(road[2])
    roads[siteA][siteB] = length
    roads[siteB][siteA] = length
    rawLength = rawLength + length
length = 0
while len(roads) != 1:
    length = findShortest(roads) + length
print(rawLength - length,end="")
