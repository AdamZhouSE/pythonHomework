from collections import Counter
num = input()
ls1 = []
ls2 = []
ls3 = []
for i in range(0, int(num)):
    ls1.append(input())
    ls2.append(input().split(" "))
    ls3.append(input())
for i in range(0, int(num)):
    countDict = Counter(ls2[i])
    countLs = []
    for j in countDict.values():
        countLs.append(j)
    finalCountLs = list(map(int, countLs))
    finalCountLs.sort()
    deleteNum = int(ls3[i])
    while deleteNum != 0:
        finalCountLs[0] -= 1
        deleteNum -= 1
        if finalCountLs[0] == 0:
            finalCountLs.pop(0)
    print(finalCountLs.__len__())