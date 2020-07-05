import sys
input()
line=input().strip(',')
matrix=[]
while(line!=']'):
    matrix.append(eval(line))
    line=input().strip(',')
trees=[]
for i in matrix:
    for j in i:
        if(j>0 and j not in trees):
            trees.append(j)
trees.sort()
route=0
m=len(matrix)
n=len(matrix[0])
distances=[[-1]*n for i in range(m)]
def search(target,i,j,record):
    global matrix,distances,m,n
    if(matrix[i][j]==target):
        return 0
    elif(distances[i][j]!=-1):
        return distances[i][j]
    else:
        judge=False
        if (i != 0):
            if(matrix[i-1][j]!=0 and [i-1,j] not in record):
                judge=True
                record.append([i-1,j])
                dt = 1 + search(target,i-1,j,list.copy(record))
                record=record[:-1]
                if (dt != 0 and (dt < distances[i][j] or distances[i][j] == -1)):
                    distances[i][j] = dt
        if (i != m - 1):
            if(matrix[i+1][j]!=0 and [i+1,j] not in record):
                judge=True
                record.append([i+1,j])
                dt = 1 + search(target,i+1,j,list.copy(record))
                record = record[:-1]
                if (dt != 0 and (dt < distances[i][j] or distances[i][j] == -1)):
                    distances[i][j] = dt
        if (j != 0):
            if(matrix[i][j-1]!=0 and [i,j-1] not in record):
                judge=True
                record.append([i,j-1])
                dt = 1 + search(target,i,j-1,list.copy(record))
                record = record[:-1]
                if (dt != 0 and (dt < distances[i][j] or distances[i][j] == -1)):
                    distances[i][j] = dt
        if (j != n - 1):
            if(matrix[i][j+1]!=0 and [i,j+1] not in record):
                judge=True
                record.append([i,j+1])
                dt = 1 + search(target,i,j+1,list.copy(record))
                record = record[:-1]
                if (dt != 0 and (dt < distances[i][j] or distances[i][j] == -1)):
                    distances[i][j] = dt
        if(not judge):
            return -1
        else:
            return distances[i][j]


for i in range(0,len(trees)-1):
    for j in range(m):
        found=False
        for k in range(n):
            if(matrix[j][k]==trees[i]):
                temp=search(trees[i+1],j,k,[[j,k]])
                if(temp==-1):
                    print(-1)
                    sys.exit()
                route+=temp
                found=True
                break
        if(found):
            break
    distances = [[-1] * n for i in range(m)]
print(route)

