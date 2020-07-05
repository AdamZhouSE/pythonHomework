def judge(roads):
    i = 0
    while i < len(roads):
        count = 0
        for j in roads[i]:
            if j == 1:
                count = count + 1
        if count == 3:
            del roads[i]
            for j in roads:
                del j[i]
            i = i - 1
        i = i + 1
    degreeCount = 0
    for i in roads:
        count = 0
        for j in i:
            if j == 1:
                count = count + 1
        if count == 0:
            degreeCount = degreeCount + 1
    if degreeCount >= 2:
        return True
    else:
        return False
    

def delect(roads):
    length = len(roads)
    lastLength = len(roads)+1
    while length != lastLength:
        i = 0
        lastLength = length
        while i < len(roads):
            count = 0
            for j in roads[i]:
                if j == 1:
                    count = count + 1
            if count <= 1:
                length = length - 1
                del roads[i]
                for j in roads:
                    del j[i]
                i = i - 1
            i = i + 1
    return roads

def countDegree(roads):
    degreeCount = 0
    for i in range(len(roads)):
        count = 0
        for j in roads[i]:
            if j == 1:
                count = count + 1
        if count == 3:
            degreeCount = degreeCount + 1
        if count > 3:
            degreeCount = degreeCount + 3
    return degreeCount
            
        

numOfInput = int(input())
for i in range(numOfInput):
    NM = input().split(" ")
    n = int(NM[0])
    m = int(NM[1])
    roads = []
    colours = []
    for j in range(n):
        road = []
        for k in range(n):
            road.append(0)
        roads.append(road)
        colours.append(0)
    for j in range(m):
        road = input().split(" ")
        a = int(road[0])-1
        b = int(road[1])-1
        roads[a][b] = 1
        roads[b][a] = 1
    roads = delect(roads)
    degree = countDegree(roads)
    if degree > 2:
        print("NO")
    elif degree == 0:
        if len(roads)%2 == 0:
            print("YES")
        else:
            print("NO")
    else:
        if len(roads)%2 == 0:
            print("NO")
        else:
            if judge(roads):
                print("YES")
            else:
                print("NO")
    