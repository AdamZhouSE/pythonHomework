inp = input()
tmp = inp[1:len(inp) - 1]
nums = tmp.split(',')
num = [int(nums[i]) for i in range(len(nums))]
length = len(num)
dp = [1 for _ in range(length)]
for i in range(1, length):
    dp[i] = dp[i - 1] + 1
    for j in range(i):
        if num[j] > num[i]:
            dp[i] = min(dp[j:i])
            break
print(dp[-1])
