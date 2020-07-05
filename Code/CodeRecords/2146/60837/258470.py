roads = []


def create(road):
    Matrix = []
    for i in range(len(road)+1):
        List = []
        for j in range(len(road)+1):
            List.append(0)
        Matrix.append(List)
    for i in range(len(road)):
        Matrix[road[i][0] - 1][road[i][1] - 1] = road[i][2]
        Matrix[road[i][1] - 1][road[i][0] - 1] = road[i][2]
    return Matrix


def findRoad(Matrix, a, b):
    start = a
    for i in range(len(Matrix[0])):
        if Matrix[a][i] != 0:
            if i == b:
                roads.append([a, b])
            else:
                hasUsed=[a,i]
                findroad(Matrix,hasUsed, i, b )


def findroad(Matrix,hasUsed, a, b ):
    has=hasUsed
    for i in range(len(Matrix[0])):
        exist = 0
        print(has)
        if Matrix[a][i] != 0:
            if i == b:
                has.append(b)
                roads.append(has)
                continue
            for j in range(len(has)):
                if i == has[j]:
                    exist = 1
                    break
        if exist == 1:
            continue
        else:
            has.append(i)
            findroad(Matrix, has, i, b)


def findMinT(Matrix, saleWhat, k):
    t = []
    for i in range(len(roads)):
        thisT = -1
        K = 0
        if saleWhat[roads[i][0]] == 1:
            K += 1
        else:
            K -= 1
        if abs(K)>k:
            continue
        for j in range(len(roads[i] )-1):
            if saleWhat[roads[i][j + 1]] == 1:
                K += 1
            else:
                K -= 1
            if abs(K) > k:
                break
            thisT = Matrix[roads[i][j]][roads[i][j + 1]]
        t.append(thisT)
    Min = max(t)
    for i in range(len(t)):
        if t[i] == -1:
            continue
        if t[i] < Min:
            Min = t[i]
    return Min


T = int(input())
nmk = list(map(int,input().split(' ')))
k = nmk[2]
saleWhat = list(map(int,input().split(' ')))
road = []
for i in range(nmk[1]):
    road.append(list(map(int, input().split(' '))))
ab = list(map(int, input().split(' ')))
a = ab[0]
b = ab[1]
Matrix = create(road)
findRoad(Matrix, a - 1, b - 1)
print(findMinT(Matrix,saleWhat,k))