def findMin(nums,start,end):
    if int(nums[start])<int(nums[end]):
        return nums[start]
    elif end-start != 1:
        mid = int((start+end)/2)
        if int(nums[mid])>=int(nums[start]):
            return findMin(nums,mid,end)
        else:
            return findMin(nums,start,mid)
    else:
        return nums[end]
    
nums = input().split(",")
print(findMin(nums,0,len(nums)-1))
    