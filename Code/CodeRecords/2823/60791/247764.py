n,k = [int(i) for i in input().split()]
x = 2005
MOD = 1000000007
dp = [None]*x

for i in range(len(dp)):

	dp[i] = [0]*x

for i in range(0,n+1):
	dp[1][i] = 1
for i in range(1,k):
	for j in range(1,n+1):
		m = j
		while(m<=n):
			dp[i+1][m] = (dp[i+1][m]+dp[i][j])%MOD
			m+=j
ans = 0
for i in range(1,n+1):
	ans = (ans+dp[k][i])%MOD
print(ans)
    