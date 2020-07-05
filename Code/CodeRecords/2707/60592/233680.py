nums = eval(input())
count = 0
for i in range(0,len(nums),2):
    if nums[i] % 2 == 0:
        if nums[i+1] == nums[i]+1:
            continue
        for j in range(0,len(nums)):
            if nums[j] == nums[i]+1:
                temp = nums[j]
                nums[j] = nums[i+1]
                nums[i+1] = temp
                count+=1
                break
    elif nums[i] % 2 == 1:
        if nums[i] == nums[i+1]+1:
            continue
        for j in range(0,len(nums)):
            if nums[j] == nums[i]-1:
                temp = nums[j]
                nums[j] = nums[i+1]
                nums[i+1] = temp
                count+=1
                break
print(count)