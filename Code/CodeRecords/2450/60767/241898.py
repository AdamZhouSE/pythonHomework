def getLeftBound(nums,target):
    left = 0
    right = len(nums)
    while(left<right):
        mid = int((right+left)/2)
        if(nums[mid]==target):
            right = mid
        elif(nums[mid]<target):
            left = mid + 1
        elif(nums[mid]>target):
            right = mid
    return left

def getRightBound(nums,target):
    left = 0
    right = len(nums)
    while(left<right):
        mid = int((right + left) / 2)
        if(nums[mid]==target):
            left = mid + 1
        elif (nums[mid] < target):
            left = mid + 1
        elif (nums[mid] > target):
            right = mid
    return left-1

inp = input().split(",")
nums = []
for i in inp:
    nums.append(int(i))
target = int(input())
res = []
if(target not in nums):
    res.append(-1)
    res.append(-1)
else:
    res.append(getLeftBound(nums,target))
    res.append(getRightBound(nums,target))
print(res)