def findProperIdx(nums,lo,hi,target):
    while lo<hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target: return mid
        if target < nums[mid]: hi=mid-1
        else: lo=mid+1
    if nums[lo]<target: return lo+1
    else: return lo


nums=[int(x) for x in input().split(',')]
print(findProperIdx(nums,0,len(nums)-1,int(input())))
