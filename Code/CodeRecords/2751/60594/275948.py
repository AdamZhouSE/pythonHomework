def updateMatrix(matrix):
    if matrix == []:
        return []
    m, n = len(matrix), len(matrix[0])
    dp = [[float('inf')] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if matrix[i][j] == 0:
                dp[i][j] = 0
            else:
                if i < m - 1:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                if j < n - 1:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
    return dp
matrix=[]
while(True):
    try:
        row=[int(n) for n in input().split()]
        matrix.append(row)
    except EOFError:
        break
ans=updateMatrix(matrix)
if ans==[]:
    print([])
else:
    for i in ans:
        for j in range(len(i)-1):
            print(i[j],end=" ")
        print(i[len(i)-1])