a = [int(x) for x in input().split(' ')]
res = []
for i in range(a[1]):
    res.append([int(x) for x in input().split(' ')])
dp = [[0]*(a[0]+2) for _ in range(1000)]
ans = []
for i in range(len(res)):
    for j in range(len(res)):
        l = res[i]
        r = res[j]
        for x in range(len(l)):
            for y in range(len(r)):
                if l[x] == r[y]:
                    dp[x + 1][y + 1] = dp[x][y] + 1
                else:
                    dp[x+1][y+1] = max(dp[x][y+1], dp[x+1][y])
        ans.append(dp[a[0]][a[0]])
print(min(ans))



