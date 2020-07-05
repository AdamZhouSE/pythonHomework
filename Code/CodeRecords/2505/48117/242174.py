numList = input().split(',')

for index in range(len(numList)):
    num = numList[index]
    del numList[index]
    if num in numList:
        break
print(num)