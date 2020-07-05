def findRoad(times,goods,loc,foodWater,hasReach,target,limit):
    if [loc,foodWater] in hasReach:
        return -1
    hasReach.append([loc,foodWater])
    if goods[loc] == 1:
        foodWater = foodWater + 1
    else:
        foodWater = foodWater - 1
    if foodWater>limit or foodWater<-limit:
        return -1
    minTime = -1
    if loc == target:
        return 0
    for i in range(len(times[loc])):
        if times[loc][i] != 0:
            time = findRoad(times,goods,i,foodWater,hasReach,target,limit)
            if time != -1:
                time = time + times[loc][i]
            if minTime == -1:
                minTime = time
            elif time < minTime and time != -1:
                minTime = time
    return minTime

numOfInput = int(input())
for i in range(numOfInput):
    NMK = input().split(" ")
    n = int(NMK[0])
    m = int(NMK[1])
    k = int(NMK[2])
    times = []
    for j in range(n):
        time = []
        for j in range(n):
            time.append(0)
        times.append(time)
    goods = list(map(int,input().split(" ")))
    for j in range(m):
        road = input().split(" ")
        a = int(road[0])
        b = int(road[1])
        time = int(road[2])
        times[a-1][b-1] = time
        times[b-1][a-1] = time
    target = input().split(" ")
    start = int(target[0])-1
    end = int(target[1])-1
    print(findRoad(times,goods,start,0,[],end,k))
    