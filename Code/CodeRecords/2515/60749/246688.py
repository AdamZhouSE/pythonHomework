def cansplit(nums, m, sum):
    count=1
    s=0
    for num in nums:
        s+=num
        if s>sum:
            count+=1
            s=sum
    return count<=m
def splitarray(nums,m):
    n=len(nums)
    left=0.0
    right=0.0
    for num in nums:
        left=max(left,num)
        right+=num
    while left<=right:
        mid=(left+right)/2
        if cansplit(nums,m,mid):
            right=mid-1
        else:
            left=mid+1
    return left
nums=input()
m=input()
print(splitarray(nums,m))