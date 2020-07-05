nums=eval(input())
res=0
for i in range(1,len(nums)):
    tmp=i-1
    while(tmp>=0 and nums[tmp]>nums[tmp+1]):
        x=nums[tmp]
        nums[tmp]=nums[tmp+1]
        nums[tmp+1]=x
        tmp-=1
for i in range(len(nums)-1):
    x=nums[i+1]-nums[i]
    if(x>res):
        res=x
print(res)