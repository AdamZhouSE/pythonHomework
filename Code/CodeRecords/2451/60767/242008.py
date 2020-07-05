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

inp = input().split(",")
nums = []
for i in inp:
    nums.append(int(i))
target = int(input())
print(getLeftBound(nums,target))