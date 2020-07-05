T=int(input())
result=[]
for i in range(T):
    n=int(input())
    l=list(map(int,input().split()))
    matrix=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j]=l[i*n+j]
    for i in range(n //2):
        for j in range(i, n - i - 1):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[j][n - i - 1], tmp = tmp, matrix[j][n - i - 1]
            matrix[n - i - 1][n - j - 1], tmp = tmp, matrix[n - i - 1][n - j - 1]
            matrix[n - j - 1][i] = tmp
    res=""
    for i in range(n):
        for j in range(n):
            res+=str(matrix[i][j])+" "
    result.append(res)
for item in result:
    print(item)