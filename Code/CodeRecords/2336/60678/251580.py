def findMax(numList):
    if numList == []:
        return None
    max = int(numList[0])
    for i in range(0, len(numList)):
        if int(numList[i]) > max:
            max = int(numList[i])
    return max


times = int(input())

for loopTimes in range(0, times):
    lengths = input().split()
    length = int(lengths[0])
    subLength = int(lengths[1])
    nums = input().split()
    outcomeList = []
    for i in range(0, len(nums) - subLength + 1):
        outcomeList.append(str(findMax(nums[i:i + subLength])))
    print(' '.join(outcomeList)+' ')