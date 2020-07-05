nk = input().split(' ')
n = int(nk[0])
k = int(nk[1])

nameList = []
nameNum = []

for i in range(n):
    name_num = input().split(' ')
    name = name_num[0]
    num = int(name_num[1])
    nameList.append((name, num))
    nameNum.append(num)

sameNum = []
for m in range(len(nameNum) - 1):
    if nameNum[m] == nameNum[m + 1]:
        sameNum.append(nameNum[m])

nameList = sorted(nameList, key=lambda x: x[1], reverse=True)

for j in range(k):
    interestedName = input()
    realName = interestedName
    count = 0
    returnIndex = 0
    index = 0
    while index < len(nameList):
        if interestedName == realName:
            returnIndex = index

        if nameList[index][0] == interestedName[0]:
            interestedName = interestedName[1:]
        else:
            if interestedName == realName:
                index += 1
                continue
            else:
                if nameList[index][1] in sameNum:
                    index += 1
                    continue
                else:
                    interestedName = realName
                    index = returnIndex

        if len(interestedName) == 0:
            interestedName = realName
            count += 1
            index = returnIndex
        index += 1

    print(count)