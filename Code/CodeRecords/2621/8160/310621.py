nums = input().replace("[", "").replace("]", "").split(",")
intArray = []
for each in nums:
    intArray.append(int(each))
length = len(intArray)
i = 0
result = intArray[0]
while i < length:
    sums = []
    temp = 0
    for j in range(i, length):
        temp += intArray[j]
        sums.append(temp)
    if result < max(sums):
        result = max(sums)
    i += 1
print(result)