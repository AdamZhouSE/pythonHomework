s = int(input())
nums = input().split(',')
# res = len(nums)
# for i in range(0, len(nums)):
#     tmp = 1
#     if i + 1 < len(nums):
sum = 0
dp = [len(nums)] * len(nums)
for i in range(0, len(nums)):
    sum = int(nums[i])
    if sum >= s:
        dp[i] = 1
    else:
        for j in range(i + 1, len(nums)):
            sum += int(nums[j])
            if sum >= s:
                dp[i] = j - i + 1
                break
print(min(dp))
