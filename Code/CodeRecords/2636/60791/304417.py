n,m = [int(i) for i in input().split(' ')]
graph = [[0 for i in range(n)] for i in range(n)]


for time in range(m):
    x,y,length = [int(i)-1 for i in input().split(' ')]
    length += 1
    graph[x][y] = length
    graph[y][x] = length

for times in range(n-2):
    for i in range(n):
        for j in range(n):
            for h in range(n):
                if graph[i][j] != 0 and graph[j][h] != 0 and i!=h:
                    if graph[i][h] == 0:
                        graph[i][h] = graph[i][j] + graph[j][h]
                        graph[h][i] = graph[i][j] + graph[j][h]
                    else:
                        graph[i][h] = min( graph[i][j] + graph[j][h],graph[i][h])
                        graph[h][i] = min( graph[i][j] + graph[j][h],graph[i][h])

T = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for h in range(j+1,n):
            ma = max(graph[i][j],graph[i][h],graph[j][h])
            mi = min(graph[i][j],graph[i][h],graph[j][h])
            T = max(T,mi+ma)
print(T)