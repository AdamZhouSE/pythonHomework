import sys
lines=sys.stdin.readlines()
matrix=[]
for i in lines:
    matrix.append(i.strip('\n').split(' '))
m=len(matrix)
n=len(matrix[0])
distance=[[-1]*n for i in range(m)]
for i in range(m):
    for j in range(n):
        if(matrix[i][j]=='0'):
            distance[i][j]=0
def find_route(i,j,record):
    global m,n,distance
    if(distance[i][j]==-1):
        if(i!=0):
            if([i-1,j] not in record):
                record.append([i-1,j])
                dt=1+find_route(i-1,j,list.copy(record))
                record = record[:-1]
                if(dt < distance[i][j] or distance[i][j]==-1):
                    distance[i][j]= dt
        if(i!=m-1):
            if ([i+1, j] not in record):
                record.append([i+1, j])
                dt=1+find_route(i+1,j,list.copy(record))
                record = record[:-1]
                if (dt < distance[i][j] or distance[i][j]==-1):
                    distance[i][j] = dt
        if(j!=0):
            if ([i, j-1] not in record):
                record.append([i, j-1])
                dt=1+find_route(i,j-1,list.copy(record))
                record=record[:-1]
                if (dt < distance[i][j] or distance[i][j]==-1):
                    distance[i][j] = dt
        if(j!=n-1):
            if ([i, j+1] not in record):
                record.append([i, j+1])
                dt+=find_route(i,j+1,list.copy(record))
                record = record[:-1]
                if (dt < distance[i][j] or distance[i][j]==-1):
                    distance[i][j] = dt
    return distance[i][j]
for i in range(m):
    for j in range(n):
        find_route(i,j,[[i,j]])
for i in range(m):
    for j in range(n):
        if(j!=n-1):
            print(distance[i][j],end=' ')
        else:
            print(distance[i][j])