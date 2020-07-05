def findOnce(nums,start,end):
    mid = int((start+end)/2)
    mid2 = 2 * mid
    if nums[mid2-1]!=nums[mid2] and nums[mid2]!=nums[mid2+1]:
        return nums[mid2]
    elif nums[mid2-1] == nums[mid2]:
        return findOnce(nums,start,mid-1)
    else:
        return findOnce(nums,mid+1,end)
    
nums = input().strip("[]").split(",")
print(findOnce(nums,0,int(len(nums)/2)))