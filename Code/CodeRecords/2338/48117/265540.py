questNum = int(input())

for i in range(questNum):
    nt = input().split(' ')
    n = int(nt[0])
    t = int(nt[1])
    numList = input().split(' ')
    hasPair = False

    for index in range(len(numList)):
        numList[index] = int(numList[index])

    for num in range(len(numList)):
        restT = t - numList[num]
        nowNum = numList[num]
        del numList[num]
        if restT in numList:
            hasPair = True
            break
        numList.append(nowNum)

    if hasPair:
        print('Yes')
    else:
        print('No')