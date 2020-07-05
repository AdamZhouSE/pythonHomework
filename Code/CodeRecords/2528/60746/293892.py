def Ascend(nums:list):
    n=len(nums)
    for i in range(0,n):
        for p in range(i+1,n):
            if nums[i]>nums[p]:
                t=nums[i]
                nums[i]=nums[p]
                nums[p]=t
    return nums
nums=[5,1,1,2,0,0]
print(Ascend(nums))
        