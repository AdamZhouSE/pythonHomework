def insertSort(nums):
    for i in range (1,len(nums)):
        temp = nums[i]
        j = i
        while(j>0 and temp<nums[j-1]):
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = temp
    return nums

temp = input()[1:-1].split(",")
nums = []
for t in temp:
    nums.append(int(t))
print(insertSort(nums))

