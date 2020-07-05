nums=input()[1:-1].split(",")
nums=list(map(int,nums))
for i in range(len(nums)-1):
    j=i+1
    min=i
    while j<len(nums):
        if nums[j]<nums[min]:
            min=j
        j=j+1
    if min!=i:
        temp=nums[i]
        nums[i]=nums[min]
        nums[min]=temp
print(nums)