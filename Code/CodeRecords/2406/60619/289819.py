length = int(input())
num = []
for i in range(length):
    num.append(int(input()))
result = []
for i in range(length-1):
    for j in range(i+1, length):
        tempList = []
        for k in range(length):
            tempList.append(num[k])
        temp = tempList[i]
        tempList[i] = tempList[j]
        tempList[j] = temp
        count = 0
        l = length - 1
        while l > 0:
            for m in range(l):
                if tempList[m] > tempList[m + 1]:
                    temp = tempList[m + 1]
                    tempList[m + 1] = tempList[m]
                    tempList[m] = temp
                    count += 1
            l -= 1
        result.append(count)
result.sort()
print(result[0])
