def check(x1,y1,x2,y2):
    afterGraph = graph[x1 - 1:x2]
    for x in range(len(afterGraph)):
        afterGraph[x] = afterGraph[x][y1-1:y2]
    a = len(afterGraph)
    b = len(afterGraph[0])
    point = 0
    edge = 0
    for x in range(a):
        for y in range(b):
            if(afterGraph[x][y] == 1):
                point += 1
                if(x >= 1 and afterGraph[x - 1][y] == 1):#左侧
                    edge += 1
                if (x < a - 1 and afterGraph[x + 1][y] == 1):#右侧
                    edge += 1
                if (y >= 1 and afterGraph[x][y - 1] == 1):
                    edge += 1
                if (y < b - 1 and afterGraph[x][y + 1] == 1):
                    edge += 1
    return int(point - int(edge/2))


N,M,Q = list(map(int,input().split(" ")))
graph = []
while(N != 0):
    temp = list(map(int,list(input().strip())))
    graph.append(temp)
    N -= 1
while(Q != 0):
    x1,y1,x2,y2 = list(map(int,input().split(" ")))
    print(check(x1,y1,x2,y2))
    Q -= 1