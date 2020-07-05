size = int(input())
strList = input().split()
intList = []
for var in strList:
    intList.append(int(var))
i = 0
resultList = []
while i < size - 1:
    j = 0
    aAll = 0
    while j < i + 1:
        aAll = aAll + intList[j]
        j += 1
    k = size - 1
    bAll = 0
    while k >= i + 1:
        bAll = bAll + intList[k]
        k -= 1
    result = aAll - bAll
    resultList.append(result)
    i += 1
result = 0
for val in intList:
    result += val
resultList.append(abs(result))
resultList.sort()
print(resultList[len(resultList) - 1])