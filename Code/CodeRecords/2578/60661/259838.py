nums=eval(input())
threshold=eval(input())
if type(nums)==int:
    nums=[nums]
l,r,res=1,max(nums)+1,-1
while l<=r:
    mid=(l+r)//2
    total=sum((x-1)//mid+1 for x in nums)
    if total<=threshold:
        res=mid
        r=mid-1
    else:
        l=mid+1
print(res)