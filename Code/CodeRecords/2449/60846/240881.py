def searchInRotatedArray(nums,lo,hi,target):
    if lo>hi: return -1
    mid=lo+(hi-lo)//2
    if nums[mid]==target: return mid
    if(nums[mid]<nums[hi]): #compare with the right element,because of the situation of two elements
        if nums[mid]<target and target<=nums[hi]:
            return searchInRotatedArray(nums,mid+1,hi,target)
        else:
            return searchInRotatedArray(nums,lo,mid-1,target)
    else:
        if nums[lo]<=target and target<nums[mid]:
            return searchInRotatedArray(nums,lo,mid-1,target)
        else:
            return searchInRotatedArray(nums,mid+1,hi,target)

list=[int(x) for x in input().split(',')]
target=int(input())
print(searchInRotatedArray(list,0,len(list)-1,target))