N=list(input())
nums=[]
nn=len(N)
for i in range(nn):
    k=N[i]
    if k.isdecimal():
        nums.append(int(k))
def Ascend(nums:list):
    n=len(nums)
    for i in range(0,n):
        for p in range(i+1,n):
            if nums[i]>nums[p]:
                t=nums[i]
                nums[i]=nums[p]
                nums[p]=t
    for i in range(0,n):
        nums[i]=int(nums[i])
    print(nums)
    return nums
Ascend(nums)