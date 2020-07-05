nums=input().split(",")
nums[0]=nums[0][1:len(nums[0])]
nums[-1]=nums[-1][0:-1]
nums_=[]
for i in nums:
    nums_.append(int(i))
left=0
right=len(nums_)-1
while(left<right):
    mid=(left+right)//2
    if nums_[mid-1]==nums_[mid]:
        if (mid-left)%2==1:#在右
            left=mid+1
        else:
            right=mid-2
    elif nums_[mid+1]==nums_[mid]:
        if (mid-left)%2==1:#在左
            right=mid-1
        else:
            left=mid+2
    else:
        left=mid
        right=mid
print(nums_[left])