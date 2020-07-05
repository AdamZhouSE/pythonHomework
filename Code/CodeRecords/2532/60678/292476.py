def getPosition(num, nums):
    temp = nums.copy()
    temp.sort()
    return temp.index(num)


def maxBefore(index, nums):
    oldMax = nums[0]
    for i in range(index + 1):
        if nums[i] > oldMax:
            oldMax = nums[i]
    return oldMax

def judge():
    count = 0
    nums = eval(input())
    shouldBE = []
    for i in range(len(nums)):
        shouldBE.append(getPosition(nums[i], nums))

    index = 0
    maxP = 0
    while index < len(nums):
        if shouldBE[index] > index:
            maxP = maxBefore(index, shouldBE)
            while maxP < maxBefore(maxP, shouldBE):
                maxP = maxBefore(maxP, shouldBE)
        index = maxP + 1
        count += 1
    return count