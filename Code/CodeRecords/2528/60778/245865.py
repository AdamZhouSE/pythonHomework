nums=eval(input())
for i in range(1,len(nums)):
    tmp=i-1
    while(nums[tmp]>nums[tmp+1]):
        x=nums[tmp]
        nums[tmp]=nums[tmp+1]
        nums[tmp+1]=x
        tmp-=1
print(nums)