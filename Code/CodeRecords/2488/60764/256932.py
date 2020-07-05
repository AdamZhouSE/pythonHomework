nums=list(eval(input()))
nums.sort()
if len(nums)<=2:
    print(nums)
else:
    for i in range(1,len(nums),2):
        if i+1<len(nums):
            tem=nums[i+1]
            nums[i+1]=nums[i]
            nums[i]=tem
    print(nums)