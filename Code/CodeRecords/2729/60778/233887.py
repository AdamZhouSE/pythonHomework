
def find(nums):
    size=len(nums)
    if(size==1):
        return nums
    if(nums[size//2]==nums[size//2+1]):
        if((size-1%4)==0):
            return find(nums[size//2:size])
        else:
            return find(nums[0:size//2])
    else:
        if((size-1%4)==0):
           return find(nums[0:size//2+1])
        else:
           return find(nums[size//2+1:size])
           
nums=input()
res=find(nums)
print(res)
