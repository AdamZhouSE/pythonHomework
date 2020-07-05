numList = input().split(',')

for index in range(len(numList)):
    num = numList[index]
    numList[index] = ','
    if num in numList:
        break
print(num)