def midSearch(startPosition, endPosition, target, nums):
    midPosition = (startPosition + endPosition) // 2
    if target == nums[midPosition]:
        return midPosition
    if nums[midPosition] > target:
        return midSearch(startPosition, midPosition - 1, target, nums)
    elif nums[midPosition] < target:
        return midSearch(midPosition + 1, endPosition, target, nums)
    else:
        return  -1


nums = eval(input())
target = int(input())
print(midSearch(0,len(nums) - 1, target, nums))