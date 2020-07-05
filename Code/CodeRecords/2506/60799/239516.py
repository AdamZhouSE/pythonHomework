aList = [int(i) for i in input().split(',')]
bList = [1] * len(aList)
for i in range(len(aList)):
    for j in range(i):
        if aList[i] > aList[j]:
            bList[i] = max(bList[j]+1, bList[i])
print(bList[-1])