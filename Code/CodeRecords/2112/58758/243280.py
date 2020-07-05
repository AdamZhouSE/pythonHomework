nums = input().split(',')
for i in range(0, len(nums)):
    if int(nums[i]) != i+1:
        temp = nums[int(nums[i])-1]
        nums[int(nums[i])-1] = nums[i]
        nums[i] = temp
print(nums.index('0'))
