def findMaxGap(arrangedList):
    maxGap = 0
    for index in range(len(arrangedList) - 1):
        if len(arrangedList) < 2:
            break
        else:
            maxGap = max(maxGap, abs(arrangedList[index + 1] - arrangedList[index]))
    return maxGap

randomList = input()
randomList = randomList[1:-1].split(",")
arrangedList = []
for num in randomList:
    trueNums = 0
    for i in range(len(num)):
        trueNums += pow(10, len(num) - 1 - i) * int(num[i])

    arrangedList.append(trueNums)
arrangedList.sort()
print(findMaxGap(arrangedList))