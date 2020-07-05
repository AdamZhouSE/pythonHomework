size = int(input())
strList = input().split()
intList = []
for var in strList:
    intList.append(int(var))
intList.sort()
i = 0
result = 0
while i < (len(intList)) // 2:
    a = intList[i] + intList[len(intList) - 1 - i]
    result += a ** 2
    i += 1
print(result)