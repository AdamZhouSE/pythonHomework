def search(ls: list) -> int:
    dp = [1] * len(ls)
    for i in range(1, len(ls)):
        for j in range(0, i):
            if ls[i] > ls[j]:
                dp[i] = max(dp[j]+1, dp[i])
    return dp[len(ls)-1]


lst = input().split(',')
lst = list(map(int, lst))
print(search(lst))