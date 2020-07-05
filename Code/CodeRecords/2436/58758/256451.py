nums = eval(input())
pair = eval(input())
nums.append(pair)
nums.sort()
i = 0
while i < len(nums)-1:
    if nums[i][1] >= nums[i+1][0]:
        if nums[i][1] < nums[i+1][1]:
            nums[i][1] = nums[i+1][1]
        nums.pop(i+1)
    else:
        i += 1
print(nums)
