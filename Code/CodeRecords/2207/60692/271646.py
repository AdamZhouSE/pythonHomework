num = int(input())
res = []
for i in range(num):
    list1 = input().split(" ")
    a = int(list1[0])
    b = int(list1[1])
    dp = [[0] * (a + 1) for m in range(a + 1)]
    dp[0][0] = 1
    for i in range(1, a + 1):
        for j in range(1, i + 1):
            dp[i][j] = dp[i - j][j] + dp[i - j][j - 1]
    if dp[a][b]:
        res.append(1)
    else:
        res.append(0)
for i in res:
    print(i)