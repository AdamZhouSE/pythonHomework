nums=eval(input())
for i in range(1,len(nums)):
    if nums[i]<nums[i-1]:
        print(nums[i])
        exit()
print(nums[0])