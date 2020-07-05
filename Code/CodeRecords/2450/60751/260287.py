nums=input().split(",")
target=int(input())
nums_=[]
for i in nums:
    nums_.append(int(i))
def find(head,end,target,nums):
    if head>end:
        return [-1,-1]
    mid=(head+end)//2
    a=0
    b=0
    if nums[mid]==target:
        for i in range(0,mid):
            if nums[mid-i-1]!=target:
                a=mid-i
                break
        for i in range(mid+1,len(nums)):
            if nums[i]!=target:
                b=i-1
                break
        return [a,b]
    elif nums[mid]>target:
        return find(head,mid-1,target,nums)
    else:
        return find(mid+1,end,target,nums)
print(find(0,len(nums_)-1,target,nums_))

