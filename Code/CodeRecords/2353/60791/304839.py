n,m = [int(i) for i in input().split(' ')]

graph1 = [[0 for i in range(n)] for i in range(n)]
graph2 = [[0 for i in range(m)] for i in range(m)]
for time in range(n-1):
    
    temp = input().split(' ')
    x,y = int(temp[0])-1,int(temp[1])-1
    graph1[x][y] = 1
    graph1[y][x] = 1
     
for time in range(m-1):
    temp = input().split(' ')
    x,y = int(temp[0])-1,int(temp[1])-1
    graph2[x][y] = 1
    graph2[y][x] = 1
for times in range(n-2):
    for i in range(n):
        for j in range(n):
            for h in range(n):
                if graph1[i][j] != 0 and graph1[j][h] != 0 and i!=h:
                    if graph1[i][h] == 0:
                        graph1[i][h] = graph1[i][j] + graph1[j][h]
                        graph1[h][i] = graph1[i][j] + graph1[j][h]
                    else:
                        graph1[i][h] = min( graph1[i][j] + graph1[j][h],graph1[i][h])
                        graph1[h][i] = min( graph1[i][j] + graph1[j][h],graph1[i][h])
for times in range(m-2):
    for i in range(m):
        for j in range(m):
            for h in range(m):
                if graph2[i][j] != 0 and graph2[j][h] != 0 and i!=h:
                    if graph2[i][h] == 0:
                        graph2[i][h] = graph2[i][j] + graph2[j][h]
                        graph2[h][i] = graph2[i][j] + graph2[j][h]
                    else:
                        graph2[i][h] = min( graph2[i][j] + graph2[j][h],graph2[i][h])
                        graph2[h][i] = min( graph2[i][j] + graph2[j][h],graph2[i][h])
                        

res = 0
for i in range(n):
    ma1 = 0
    for item in graph1[i]:
        ma1 = max(ma1,item)
    for j in range(m):
        res += ma1
        ma = 0
        for item in graph2[j]:
            ma = max(ma,item)
        res += ma+1
print(res)
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        