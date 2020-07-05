t = int(input())
for k in range(t):
    m, n = map(int, input().split())
    a = [[1] * m for i in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            a[i][j] = a[i][j - 1] + a[i - 1][j]
    print(a[n - 1][m - 1])
