def d(lett1, lett2, s1):
    str1 = letter_s[lett1 - 1]
    str2 = letter_s[lett2 - 1]
    s = str1 + str2
    if s1.find(s) == -1:
        return 1
    else:
        return 0


s2_len = int(input())
s1 = input()
letter_s = 'abcdefghijklmnopqrstuvwxyz'
ans = 0
# 初始化dp都是不用0的
dp = []
for i in range(s2_len + 1):
    dp.append([])
for i in range(1, s2_len + 1):
    for j in range(26 + 1):
        dp[i].append(1)
# 完成了初始化dp and i为1时候，值为1
for i in range(2, s2_len + 1):
    for j in range(1, 26 + 1):
        ans = 0
        for k in range(1, 26 + 1):
            ans += dp[i - 1][k] * d(k, j, s1)
        dp[i][j] = ans
ans = 0
for i in range(1, 26 + 1):
    ans += dp[s2_len][i]
print(ans)
