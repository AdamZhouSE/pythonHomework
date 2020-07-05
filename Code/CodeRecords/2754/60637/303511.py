grid=eval(input())
n=len(grid)
m=len(grid[0])
distance=[[-1]*m for i in range(n)]
def search_land(record,i,j):
    global grid,distance
    if(grid[i][j]==1):
        distance[i][j]=0
    else:
        judge=False
        if (i != 0 and [i - 1, j] not in record):
            record.append([i - 1, j])
            dp = 1 + search_land(list.copy(record), i - 1, j)
            if (dp!=-1 and(dp < distance[i][j] or distance[i][j] == -1)):
                distance[i][j] = dp
                judge = True
            record = record[:-1]
        if (i != n-1 and [i + 1, j] not in record):
            record.append([i + 1, j])
            dp = 1 + search_land(list.copy(record), i + 1, j)
            if (dp!=-1 and(dp < distance[i][j] or distance[i][j] == -1)):
                distance[i][j] = dp
                judge = True
            record = record[:-1]
        if (j != 0 and [i, j - 1] not in record):
            record.append([i, j - 1])
            dp = 1 + search_land(list.copy(record), i, j - 1)
            if (dp!=-1 and(dp < distance[i][j] or distance[i][j] == -1)):
                distance[i][j] = dp
                judge = True
            record = record[:-1]
        if (j != m-1 and [i, j + 1] not in record):
            record.append([i, j + 1])
            dp = 1 + search_land(list.copy(record), i, j + 1)
            if (dp!=-1 and(dp < distance[i][j] or distance[i][j] == -1)):
                distance[i][j] = dp
                judge = True
            record = record[:-1]
        if(not judge):
            return -2
    return distance[i][j]
for i in range(n):
    for j in range(m):
            search_land([[i,j]],i,j)
record=-1
for i in range(n):
    for j in range(m):
        if(distance[i][j]!=0 and distance[i][j]>record):
            record=distance[i][j]
print(record)
