def longestCommonString(str1, str2) -> str:
    m = len(str1)
    n = len(str2)
    res = ''
    ans = 0
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    ans = dp[-1][-1]
    i = m
    j = n
    while i > 0 and j > 0:
        if dp[i][j - 1] == dp[i][j] - 1 and dp[i - 1][j] == dp[i][j] - 1:
            res = str1[i - 1] + res
            j -= 1
            i -= 1
        elif dp[i][j - 1] == dp[i][j]:
            j -= 1
        elif dp[i - 1][j] == dp[i][j]:
            i -= 1

    return res


T = eval(input())
for i in range(T):
    str1, str2 = input().split()
    LCS = longestCommonString(str1, str2)
    print(len(str1) + len(str2) - len(LCS))