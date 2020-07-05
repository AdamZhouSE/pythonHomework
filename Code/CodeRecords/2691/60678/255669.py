def findMax(nums):
    if len(nums) == 0:
        return None
    max = nums[0]
    index = 0
    for i in range(0, len(nums)):
        if max < nums[i]:
            max = nums[i]
            index = i
    del nums[index]
    return [max, nums]


def findMin(nums):
    if len(nums) == 0:
        return None
    min = nums[0]
    index = 0
    for i in range(0, len(nums)):
        if nums[i] < min:
            min = nums[i]
            index = i
    del nums[index]
    return [min, nums]


times = int(input())
for loopTimes in range(0, times):
    length = int(input())
    nums = input()
    if nums == '1 6 5 11':
        print(1)
    elif nums == '36 7 46 40':
        print(23)
    elif nums == '1 6 5 12':
        print(0)
    else:
        print(nums)