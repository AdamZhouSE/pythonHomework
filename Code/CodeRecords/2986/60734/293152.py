begin = input()
end = input()

dp = [[len(begin) for i in range(len(begin))] for j in range(len(end))]
if begin[0]==end[0]:
    dp[0][0] = 0
else:
    dp[0][0] = 1
for i in range(1,len(begin)):
    dp[0][i] = dp[0][i-1]+1
for j in range(1,len(end)):
    dp[j][0] = dp[j-1][0]+1

for i in range(1,len(end)):
    for j in range(1,len(begin)):
        if begin[j] == end[i]:
            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1])
        else:
            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)

print(dp[len(end)-1][len(begin)-1])