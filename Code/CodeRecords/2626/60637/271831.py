nums=input().split(',')
handle_nums=[1]
for i in nums:
    handle_nums.append((int)(i))
handle_nums+=[1]
n=len(handle_nums)
dp=[[(int)(0)]*n for i in range(0,n)]
for l in range(2,n):
    	for i in range(n-1):
    		if i+l <n:
    			for k in range(i+1,i+l):
    				dp[i][i+l] = max(dp[i][i+l],dp[i][k]+dp[k][i+l]+handle_nums[i]*handle_nums[k]*handle_nums[i+l])
print(dp[0][n-1])