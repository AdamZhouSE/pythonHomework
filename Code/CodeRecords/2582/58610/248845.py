a, b = eval(input()), eval(input())
dp = [[], [], [], []]
for i in range(len(a)):
    dp[0].append(a[i] + b[i] + i)
    dp[1].append((a[i] + b[i] - i))
    dp[2].append(a[i] - b[i] + i)
    dp[3].append(a[i] - b[i] - i)
res = max([max(dp[i]) - min(dp[i]) for i in range(4)])
print(res)