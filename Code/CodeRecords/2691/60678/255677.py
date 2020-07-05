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
    nums = input().split()
    abelArray = []
    abekCount = 0
    betaArray = []
    betaCount = 0

    for i in range(0, len(nums)):
        nums[i] = int(nums[i])

    for i in range(0, len(nums) // 4):
        outcome = findMax(nums)
        abelArray.append(outcome[0])
        abekCount += outcome[0]
        nums = outcome[1]

        outcome = findMin(nums)
        abelArray.append(outcome[0])
        abekCount += outcome[0]
        nums = outcome[1]

        outcome = findMax(nums)
        betaArray.append(outcome[0])
        betaCount += outcome[0]
        nums = outcome[1]

        outcome = findMin(nums)
        betaArray.append(outcome[0])
        betaCount += outcome[0]
        nums = outcome[1]

    while len(nums) > 0:
        outcome =findMin(nums)
        if abekCount > betaCount:
            betaArray.append(outcome[0])
            nums = outcome[1]
            betaCount += outcome[0]
        else:
            abelArray.append(outcome[0])
            nums = outcome[1]
            abekCount += outcome[0]
    print(abs(abekCount - betaCount))