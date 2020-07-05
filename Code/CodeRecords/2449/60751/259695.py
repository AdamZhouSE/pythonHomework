nums=input().split(",")
target=int(input())
nums_=[]
for i in nums:
    nums_.append(int(i))
def find(head,end,target,nums):
    if head>end:
        return -1
    mid=(head+end)//2
    if nums[mid]==target:
        return mid
    elif nums[mid]<nums[end]:#右侧有序
        if target>nums[mid] and target<=nums[end]:
            return find(mid+1,end,target,nums)
        else:
            return find(head,mid-1,target,nums)
    else:
        if target<nums[mid] and target>=nums[head]:
            return find(head,mid-1,target,nums)
        else:
            return find(mid + 1, end, target, nums)
print(find(0,len(nums)-1,target,nums_))