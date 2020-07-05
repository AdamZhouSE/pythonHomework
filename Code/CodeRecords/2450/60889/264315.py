def findStart(nums,target,start,end):
    if end-start == 1:
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1
    else:
        mid = int((start+end)/2)
        if nums[mid] < target:
            return findStart(nums,target,mid,end)
        else:
            return findStart(nums,target,start,mid)
        
def findEnd(nums,target,start,end):
    if end-start == 1:
        if nums[end] == target:
            return end
        elif nums[start] == target:
            return start
        else:
            return -1
    else:
        mid = int((start+end)/2)
        if nums[mid] > target:
            return findEnd(nums,target,start,mid)
        else:
            return findEnd(nums,target,mid,end)
        
nums = input().split(",")
target = input()
start = 0;
end = len(nums)
if len(nums)==0:
    print("[-1,-1]")
else:
    start = str(findStart(nums,target,0,len(nums)-1))
    end = str(findEnd(nums,target,0,len(nums)-1))
    print("[" + start + ", " + end + "]")
        
    
