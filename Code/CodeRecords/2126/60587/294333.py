nums = input().split(',')
num = [int(nums[i]) for i in range(len(nums))]
num.sort()
dp = [[x] for x in num]
maxseq = []
for i in range(len(num)):
    for j in range(i):
        if num[i] % num[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
            dp[i] = dp[j] + num[i:i + 1]
    if len(dp[i]) > len(maxseq):
        maxseq = dp[i]
print(maxseq)
