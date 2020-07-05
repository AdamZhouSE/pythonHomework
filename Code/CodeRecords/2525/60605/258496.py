startTimes = list(eval(input()))
endTimes = list(eval(input()))
profits = list(eval(input()))
n = len(profits)

allbegin = startTimes[0]
allend = endTimes[0]
for i in startTimes:
    allbegin = min(allbegin, i)
for i in endTimes:
    allend = max(allend, i)

# time     1-allend
# tochoose 0- n-1
dp = [[0 for j in range(n+1)] for i in range(allend+1)]
for c in range(n-1, -1, -1):
    for s in range(1, allend+1):
        if startTimes[c] < s:
            dp[s][c] = dp[s][c+1]
        else:
            dp[s][c] = max(dp[s][c+1], profits[c]+dp[endTimes[c]][c+1])
# print(dp)
print(dp[1][0])