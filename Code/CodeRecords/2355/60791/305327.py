import math

n,m = [int(i) for i in input().split(' ')]
val = [int(i) for i in input().split(' ')]
graph1 = [[0 for i in range(n)] for i in range(n)]
res = 999

for time in range(m):
    temp = input().split(' ')
    
    x,y = int(temp[0])-1,int(temp[1])-1
    graph1[x][y] = 1
    graph1[y][x] = 1
end = input()
re = [0,0]

for x in range(n-1):
    for y in range(x+1,n):
        if graph1[x][y] != 1:
            pass
        else:
            graph = []
            for i1 in range(n):
                temp = []
                for i2 in range(n):
                    temp.append(graph1[i1][i2])
                graph.append(temp)
                    
            
            graph[x][y] = 0
            graph[y][x] = 0
        
            for times in range(n-2):
                for i in range(n):
                    for j in range(n):
                        for h in range(n):
                            if graph[i][j] != 0 and graph[j][h] != 0 and i!=h:
                                if graph[i][h] == 0:
                                    graph[i][h] = graph[i][j] + graph[j][h]
                                    graph[h][i] = graph[i][j] + graph[j][h]
                            
            
            fir = val[0]
            sec = 0
            for i in range(1,n):
                if graph[0][i] != 0:
                    fir += val[i]
                else:
                    sec += val[i]
            if abs(fir-sec) < res:
                res = abs(fir-sec)
                re[0],re[1] = x,y
print('Case 1: ',end='')
print(res)
        
        
        
        
        
        