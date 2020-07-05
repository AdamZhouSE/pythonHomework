T = int(input())


def longest(STR: str):
    s = list(STR)
    n = len(s)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if (s[j] < s[i]):
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


for m in range(T):
    print(longest(input()))