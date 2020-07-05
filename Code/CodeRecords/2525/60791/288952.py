import bisect
start = eval(input())
end = eval(input())
pro = eval(input())
jobs = sorted(zip(start, end, pro), key=lambda v: v[1])
dp = [[0, 0]]
for s, e, p in jobs:
	i = bisect.bisect_right(dp, [s+1]) - 1
	if dp[i][1] + p > dp[-1][1]:
		dp.append([e, dp[i][1] + p])
		
print(dp[-1][1])