n=int(input())
matrix=[]
maxnum=1
for i in range(n):
    line=[1]*n
    matrix.append(line)
for i in range(1,n):
    for j in range(1,n):
        matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]
        if matrix[i][j]>maxnum:
            maxnum=matrix[i][j]
print(maxnum)
