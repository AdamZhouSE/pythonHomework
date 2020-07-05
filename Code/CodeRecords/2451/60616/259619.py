def searchInsert( nums, target):
    if nums[0] > target: return 0

    left = 0;
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            return mid

    return left
rawInput=input().split(',')
nums=[]
for item in rawInput:nums.append(int(item))
target=int(input())
print(searchInsert(nums,target))