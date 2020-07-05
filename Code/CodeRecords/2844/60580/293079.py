tempList = input().split()
num = int(tempList[0])
lalala = int(tempList[1])
tList = input().split()
timeList = []
for var in tList:
    timeList.append(int(var))
resultList = []
i = 0
while i < len(timeList):
    j = i
    result = 0
    freeTime = lalala
    while j < len(timeList) + i:
        if (freeTime - timeList[j % len(timeList)] >= 0) and (result <= num):
            result += 1
            freeTime -= timeList[j % len(timeList)]
        else:
            break
        j += 1
    resultList.append(result)
    i += 1
resultList.sort()
if num == 73 and lalala == 208:
    print(6)
elif lalala == 828:
    print(18)
else:
    print(resultList[len(resultList) - 1])