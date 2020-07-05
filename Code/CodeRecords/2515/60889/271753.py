def nGroups(nums,numOfGroup,left,right):
    if right-left==1:
        return right
    mid = int((left+right)/2)
    nowGroup = 0
    nowSummary = 0
    for i in nums:
        if i > mid:
            return nGroups(nums,numOfGroup,mid,right)
        elif nowSummary+i>mid:
            nowSummary = i
            nowGroup = nowGroup + 1
        else:
            nowSummary = nowSummary + i
    if nowGroup >= numOfGroup:
        return nGroups(nums,numOfGroup,mid,right)
    else:
        return nGroups(nums,numOfGroup,left,mid)
    

nums = input().split(",")
nums = list(map(int,nums))
numOfGroup = int(input())
left = nums[0]
right = 0
for i in nums:
    if i < left:
        left = i
    right = right + i
print(nGroups(nums,numOfGroup,left,right+1))