from collections import Counter
testNum = int(input())
tests = []
for i in range(0, testNum):
    input()
    tests.append(list(input().split(" ")))
for i in range(0, len(tests)):
    ls = tests[i]
    elemSortedLs = []
    for elem in ls:
        elemSortedLs.append("".join(sorted(list(elem))))
    #print(elemSortedLs)
    sorted(elemSortedLs)
    elemDict = Counter(elemSortedLs)
    result = [x for x in sorted(elemDict.values())]
    for y in result:
        print(y, end=" ")
        print()