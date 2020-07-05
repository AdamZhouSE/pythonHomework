nums = input()[1:-1].split(',')
for i in range(0, len(nums)):
    nums[i] =int(nums[i])

for i in range(0,len(nums)):
    if i ==0:
        if nums[i]>nums[i+1]:
            result = 0
    elif i ==len(nums)-1:
        if nums[i]>nums[i-1]:
            result = len(nums)-1
    else:
        if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
            result = i

print(result)