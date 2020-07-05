sList = sorted([int(i) for i in input().split(',')])
ptrList = [(i, 1) for i in range(len(sList))]
for i in range(len(sList)):
    for j in range(i - 1, -1, -1):
        if sList[i] % sList[j] == 0:
            ptrList[i] = (j, ptrList[j][1] + 1)
            break
ma, ptr = 0, 0
for i in range(len(ptrList)):
    if ptrList[i][1] > ma:
        ma = ptrList[i][1]
        ptr = i
res = []
while ptr != ptrList[ptr][0]:
    res.append(sList[ptr])
    ptr = ptrList[ptr][0]
print(sorted(res+[sList[ptr]]))