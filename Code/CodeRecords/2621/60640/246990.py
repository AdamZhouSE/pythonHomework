nums = list(map(int, input().split(",")))
length = len(nums)
curr_sum = nums[0]
max_sum = nums[0]
for i in range(1, length):
    curr_sum = max(nums[i], curr_sum+nums[i])
    max_sum = max(max_sum, curr_sum)
print(max_sum)
