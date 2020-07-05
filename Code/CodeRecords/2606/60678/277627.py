def midSearch(startPosition, endPosition, target, nums):
    midPosition = (startPosition + endPosition) // 2
    if nums[endPosition] < target or nums[startPosition] > target:
        return -1
    if nums[midPosition] > target:
        return midSearch(startPosition, midPosition, target, nums)
    elif nums[midPosition] < target:
        return midSearch(midPosition, endPosition, target, nums)
    else:
        return midPosition


nums = eval(input())
target = int(input())
print(midSearch(0,len(nums) - 1, target, nums))