def oneCount(l):
    result = 0
    for i in l:
        if i == 1:
            result += 1
    return result


size = int(input())
tempList = input().split()
intList = []
for var in tempList:
    intList.append(int(var))
i = 0
resultList = []
while i < size:
    j = i
    while j < size:
        k = i
        tempList = []
        for var in intList:
            tempList.append(var)
        while k <= j:
            tempList[k] = 1 - tempList[k]
            k += 1
        result = oneCount(tempList)
        resultList.append(result)
        j += 1
    i += 1
resultList.sort()
print(resultList[len(resultList) - 1])