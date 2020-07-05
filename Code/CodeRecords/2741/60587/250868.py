inp = input()
tmp = inp[1:len(inp) - 1].split(',')
nums = [int(tmp[i]) for i in range(len(tmp))]
# print(nums)
n = len(nums)
dp = [1] * n
# res = 1
for i in range(n - 1):
    if nums[i] < nums[i + 1]:
        dp[i + 1] = dp[i] + 1
print(max(dp))
