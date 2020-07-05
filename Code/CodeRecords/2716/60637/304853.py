input()
line=input()
matrix=[]
while(line!=']'):
    start=-1
    end=-1
    count=0
    for i in range(len(line)):
        if(line[i]=='\"'and count==1):
            end=i
            break
        elif(line[i]=='\"'and count==0):
            start=i+1
            count+=1
    matrix.append(line[start:end])
    line=input()
n=len(matrix)
for i in range(n):
    matrix[i]=matrix[i].replace('\\\\','\\')
m=3*n
digitize=[[0]*m for i in range(m)]
record=[]
def dfs(i,j):
    global m,record,digitize
    if (i != 0 and [i - 1, j] not in record and digitize[i-1][j]!=1):
        record.append([i - 1, j])
        dfs(i - 1, j)
    if (i != m-1 and [i + 1, j] not in record and digitize[i+1][j]!=1):
        record.append([i + 1, j])
        dfs(i + 1, j)
    if (j != 0 and [i, j - 1] not in record and digitize[i][j-1]!=1):
        record.append([i, j - 1])
        dfs(i, j - 1)
    if (j != m-1 and [i, j + 1] not in record and digitize[i][j+1]!=1):
        record.append([i, j + 1])
        dfs(i, j + 1)
for i in range(n):
    for j in range(n):
        if(matrix[i][j]=='/'):
            digitize[i*3][j*3+2]=1
            digitize[i*3+1][j*3+1]=1
            digitize[i*3+2][j*3]=1
        elif(matrix[i][j]=='\\'):
            digitize[i * 3][j * 3] = 1
            digitize[i * 3 + 1][j * 3 + 1] = 1
            digitize[i * 3 + 2][j * 3 + 2] = 1
sum=0
for i in range(m):
    for j in range(m):
        if(digitize[i][j]==0 and [i,j] not in record):
            sum+=1
            dfs(i,j)
print(sum)


