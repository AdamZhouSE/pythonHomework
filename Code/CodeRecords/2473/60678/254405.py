def getAfromBottom(numlist):
    bottom = len(numlist)

    # find the lowest
    lowest = numlist[0]
    for i in numlist:
        if i < lowest:
            lowest = i
    return lowest * bottom


def findMaxOfFixedLen(numlist, bottomLen):
    # 这里的bottomLen一定小于len(numlist)
    areas = []
    if len(numlist) < bottomLen:
        return None
    for i in range(0, len(numlist) - bottomLen + 1):
        areas.append(getAfromBottom(numlist[i:i + bottomLen]))
    areas.sort(reverse=True)
    return areas[0]


times = int(input())
for loopTimes in range(0, times):
    input()
    nums = input().split()

    if nums == '':
        print(0)
    for i in range(0, len(nums)):
        # 转化成int
        nums[i] = int(nums[i])

    outcomeAreas = []

    for i in range(1, len(nums) + 1):
        outcomeAreas.append(findMaxOfFixedLen(nums, i))
    outcomeAreas.sort(reverse=True)
    print(outcomeAreas[0])