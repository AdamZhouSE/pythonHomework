def insertSort(nums):
    for i in range (1,len(nums)):
        temp = nums[i]
        j = i
        while(j>0 and temp<nums[j-1]):
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = temp
    return nums

temp = eval(input())
nums = []
for t in temp:
    nums.append(int(t))
nums = insertSort(nums)
res = 0
for i in range(0,len(nums)-1):
    res = max(res,nums[i+1]-nums[i])
print(res)
