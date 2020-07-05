inp = input()
a = inp[1: len(inp) - 1].split(',')
a = [int(a[i]) for i in range(len(a))]
a.sort()
res = 1
dp = [1] * len(a)
for j in range(1, len(a)):
    if a[j] == a[j - 1] + 1:
        dp[j] = dp[j - 1] + 1
    res = max(res, dp[j])
print(res)
# print(a)