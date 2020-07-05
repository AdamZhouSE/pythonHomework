line=input()[1:]
matrix=[]
while(not line.isnumeric()):
    matrix.append(eval(line[:-1]))
    line=input()
k=(int)(line)
m=len(matrix)
n=len(matrix[0])
distance=[[-1]*n for i in range(m)]
distance[m-1][n-1]=0
def find_route(record,i,j,k):
    global m,n,distance
    if(distance[i][j]==-1):
        judge=False
        if (i != 0 and [i - 1, j] not in record):
            if ((matrix[i - 1][j] == 1 and k > 0) or matrix[i - 1][j] == 0):
                judge = True
                record.append([i - 1, j])
                if (matrix[i - 1][j] == 1):
                    dp=1+find_route(list.copy(record), i - 1, j, k-1)
                else:
                    dp=1+find_route(list.copy(record), i - 1, j, k)
                record = record[:-1]
                if (dp!=0 and (dp < distance[i][j] or distance[i][j] == -1)):
                    distance[i][j] = dp
        if (i != m-1 and [i + 1, j] not in record):
            if ((matrix[i + 1][j] == 1 and k > 0) or matrix[i + 1][j] == 0):
                judge = True
                record.append([i + 1, j])
                if (matrix[i + 1][j] == 1):
                    dp=1+find_route(list.copy(record), i + 1, j, k - 1)
                else:
                    dp=1+find_route(list.copy(record), i + 1, j, k)
                record = record[:-1]
                if (dp!=0 and (dp < distance[i][j] or distance[i][j] == -1)):
                    distance[i][j] = dp
        if (j != 0 and [i, j -1] not in record):
            if ((matrix[i][j - 1] == 1 and k > 0) or matrix[i][j - 1] == 0):
                judge = True
                record.append([i, j - 1])
                if (matrix[i][j - 1] == 1):
                    dp=1+find_route(list.copy(record), i, j - 1, k - 1)
                else:
                    dp=1+find_route(list.copy(record), i, j - 1, k)
                record = record[:-1]
                if (dp!=0 and (dp < distance[i][j] or distance[i][j] == -1)):
                    distance[i][j] = dp
        if (j != n-1 and [i, j + 1] not in record):
            if ((matrix[i][j + 1] == 1 and k > 0) or matrix[i][j + 1] == 0):
                judge = True
                record.append([i, j + 1])
                if (matrix[i][j + 1] == 1):
                    dp=1+find_route(list.copy(record), i, j + 1, k - 1)
                else:
                    dp=1+find_route(list.copy(record), i, j + 1, k)
                record = record[:-1]
                if (dp!=0 and (dp < distance[i][j] or distance[i][j] == -1)):
                    distance[i][j] = dp
        if(not judge):
            return -1
    return distance[i][j]
print(find_route([[0,0]],0,0,k))