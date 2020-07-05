def findMin(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]: left = mid + 1
        elif nums[mid] < nums[right]: right = mid
        else: right = right - 1 # key
    return nums[left]

nums=[int(x) for x in input().split(',')]
print(findMin(nums))