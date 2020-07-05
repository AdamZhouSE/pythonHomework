def binarySearch(nums,target,start,end,startNum):
    if start>end:
        return -1
    else:
        mid = int((start+end)/2)
        if nums[mid] == target:
            return mid
        elif (nums[mid]>=startNum)&(target<startNum):
            return binarySearch(nums,target,mid+1,end,startNum)
        elif (nums[mid]<startNum)&(target>=startNum):
            return binarySearch(nums,target,start,mid-1,startNum)
        else:
            if nums[mid] > target:
                return binarySearch(nums,target,start,mid-1,startNum)
            else:
                return binarySearch(nums,target,mid+1,end,startNum)
                
    

nums = input().split(",")
startNum = nums[0]
target = input()
if len(nums)==0:
    print(-1)
else:
    print(binarySearch(nums,target,0,len(nums)-1,startNum))
    
