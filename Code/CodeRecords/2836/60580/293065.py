def isHigh(l):
    size = len(l)
    if size == 1:
        return True
    else:
        i = 0
        while i < len(l) - 1:
            if l[i] <= l[i + 1]:
                i += 1
                continue
            else:
                return False
        return True


size = int(input())
strList = input().split()
intList = []
for var in strList:
    intList.append(int(var))
i = 0
result = 0
signal = False
while i < size:
    if not isHigh(intList):
        temp = intList[len(intList) - 1]
        del intList[len(intList) - 1]
        intList.insert(0, temp)
        result += 1
        i += 1
        continue
    else:
        signal = True
        break
if signal:
    print(result)
else:
    print(-1)