def get(n, flights, src, dest, k):
    import collections
    fde = collections.defaultdict(list)
    for f in flights:
        fde[f[1]].append([f[0], f[2]])
    dp = [[float('inf') for i in range(n)] for i in range(k+1)]
    for i in fde[dest]:
        dp[0][i[0]] = i[1]
    for t in range(1, k+1):
        for pos in range(n):
            for before in fde[pos]:
                dp[k][before[0]] = min(dp[k][before[0]], dp[k-1][pos]+before[1])
            dp[k][pos] = min(dp[k][pos], dp[k-1][pos])
    ans = dp[k][src]
    return ans if ans != float('inf') else -1



n = int(input())
flight = eval(input())
src = int(input())
dest = int(input())
k = int(input())
print(get(n, flight, src, dest, k))