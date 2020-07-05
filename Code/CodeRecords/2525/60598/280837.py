import functools

start = list(map(int, input()[1:-1].split(",")))
end = list(map(int, input()[1:-1].split(",")))
profit = list(map(int, input()[1:-1].split(",")))
total = sorted([[start[i], end[i], profit[i]] for i in range(len(start))])
dp = [total[i][2] for i in range(len(start))]
for j in range(len(start)):
    for i in range(j):
        if total[i][1] <= total[j][0]:
            dp[j] = max(dp[j], total[j][2]+dp[i])
print(max(dp))

