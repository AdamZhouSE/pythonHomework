size = int(input())
tempList = input().split()
intList = []
for var in tempList:
    intList.append(int(var))
intList.sort()
i = 0
result = 0
while i < size:
    if i == size:
        break
    else:
        result = result + intList[i + 1] - intList[i]
    i += 2
print(result)
