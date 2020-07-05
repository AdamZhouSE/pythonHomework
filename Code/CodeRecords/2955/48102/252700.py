def string_distance(string1: str, string2: str, k: int) -> int:
    len1 = len(string1)
    len2 = len(string2)
    dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
    for i in range(1, len1+1):
        dp[i][0] = i * k
    for i in range(1, len2+1):
        dp[0][i] = i * k
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            dp[i][j] = min(dp[i-1][j]+k, dp[i][j-1]+k, dp[i-1][j-1]+abs(ord(string1[i-1]) - ord(string2[j-1])))
    return dp[len1][len2]


s1 = input()
s2 = input()
num = int(input())
print(string_distance(s1, s2, num), end='')