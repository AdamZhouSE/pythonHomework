def findPeakElement( nums):
    left = 0
    right = len(nums) - 1
    while left <= right:
        if left == right:
            return left
        mid = left + (right - left) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
nums=list(map(int,input().split(',')))
print(findPeakElement(nums))