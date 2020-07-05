T = eval(input())
for i in range(T):
    n = eval(input())
    num = list(map(int,input().split(' ')))
    matrix = []
    for i in range(n):
        a = []
        for j in range(n):
            a.append(num[i*n+j])
        matrix.append(a)
    for i in range(0,n//2):
        for j in range(i,n-1-i):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = tmp
    num = []
    for i in matrix:
        for j in i:
            num.append(j)
    print(' '.join(map(str,num))+' ')




