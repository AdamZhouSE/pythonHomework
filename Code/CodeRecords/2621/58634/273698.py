# 贪心

nums = [int(i) for i in input().split(",")]
n = len(nums)
curr_sum = max_sum = nums[0]

for i in range(1, n):
    curr_sum = max(nums[i], curr_sum + nums[i])
    max_sum = max(max_sum, curr_sum)

print(max_sum)
