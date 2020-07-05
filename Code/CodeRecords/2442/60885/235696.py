nums = sorted(eval(input()))
result = 0
for i in range(len(nums)-1):
    gap = nums[i+1] - nums[i]
    if gap > result:
        result = gap
print(result)