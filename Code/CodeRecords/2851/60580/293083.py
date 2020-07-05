size = int(input())
tempList = []
resultList = []
for i in range(size):
    tempList = input().split()
    resultList.append(int(tempList[0]) + int(tempList[1]))
resultList.sort()
print(resultList[len(resultList) - 1])