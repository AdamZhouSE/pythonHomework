num=int(input())
matrix=[[0]*num for x in range(num)]
for i in range(num):
    matrix[i][0]=1
    matrix[0][i]=1
for i in range(1,num):
    for j in range(1,num):
        matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]
print(matrix[num-1][num-1])