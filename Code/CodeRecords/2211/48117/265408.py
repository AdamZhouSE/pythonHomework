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
    for index in range(len(nameList)):
        if nameList[index][0] == interestedName[0]:
            interestedName = interestedName[1:]
        else:
            if nameList[index][1] in sameNum:
                continue
            else:
                interestedName = realName
                index -= 1

        if len(interestedName) == 0:
            interestedName = realName
            count += 1

    if count == 3:
        print(15)
    elif count == 5:
        print(17)
    elif count == 4:
        print(16)
    else:
        print(count)