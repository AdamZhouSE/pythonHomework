N = int(input())
aList = input().split()
set1 = set()
resultList = []
for tail in aList:
    resultList.append(tail)
    for i in range(len(resultList)):
        set1.add(''.join(resultList[i:]))
    print(len(set1))