n = int(input())
nums = input().split(',')
num = [int(nums[i]) for i in range(len(nums))]
dp = [1]
idx = [0] * len(num)
plen = len(num)
while n > 1:
    min_ = min([dp[idx[i]] * num[i] for i in range(plen)])
    for i in range(plen):
        if min_ == dp[idx[i]] * num[i]:
            idx[i] += 1
    n -= 1
    dp.append(min_)
print(dp[-1])
