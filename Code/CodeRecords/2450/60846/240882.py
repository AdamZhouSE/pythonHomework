def binSearch(nums,lo,hi,target):
    while lo<=hi:
        mid=lo+(hi-lo)//2
        if nums[mid]==target: return mid
        if target<nums[mid]: hi=mid-1
        else: lo=mid+1
    return -1

nums=[int(x) for x in input().split(',')]
target=int(input())
idx=binSearch(nums,0,len(nums)-1,target)
if idx==-1:
    print('[-1, -1]')
else:    
    left=idx
    right=idx
    while left>=0 and nums[left]==target:
        left-=1
    while right<len(nums) and nums[right]==target:
        right+=1
    ret=[left+1,right-1]
    print(ret)