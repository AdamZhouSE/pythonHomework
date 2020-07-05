def findMin( nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[left] or nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1
    return nums[left]
nums=list(map(int,input().split(',')))
print(findMin(nums))