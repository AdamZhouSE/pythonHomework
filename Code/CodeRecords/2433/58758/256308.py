nums = eval(input())
i = 0
nums.sort()
while i < len(nums)-1:
    if nums[i][1] >= nums[i+1][0]:
        nums[i][1] = nums[i+1][1]
        nums.pop(i+1)
    else:
        i += 1
print(nums)
