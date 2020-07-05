def midSearch(startPosition, endPosition, target, nums):
    midPosition = (startPosition + endPosition) // 2
    if target == nums[midPosition]
    if nums[midPosition] > target:
        return midSearch(startPosition, midPosition, target, nums)
    elif nums[midPosition] < target:
        return midSearch(midPosition, endPosition, target, nums)
    else:
        return  -1


nums = eval(input())
target = int(input())
print(midSearch(0,len(nums) - 1, target, nums))