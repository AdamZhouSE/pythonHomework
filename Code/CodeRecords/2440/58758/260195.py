nums = eval(input())
for i in range(1, len(nums)):
    for j in range(0, i):
        if nums[i] < nums[j]:
            temp = nums[i]
            nums.pop(i)
            nums.insert(j, temp)
            flag = True
            break
print(nums)
