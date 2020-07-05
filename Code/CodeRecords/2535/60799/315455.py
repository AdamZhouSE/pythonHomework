arr = [int(i) for i in input().strip('[|]').split(',')]
newList = sorted(arr)
result = tmpSum1 = newSum2 = 0
for i in range(len(arr)):
    tmpSum1 += arr[i]
    newSum2 += newList[i]
    if tmpSum1 == newSum2:
        result += 1
        tmpSum1 = newSum2 = 0
print(result)