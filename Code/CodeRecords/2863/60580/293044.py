aList = input().split()
bList = input().split()
h = int(aList[1])
result = len(bList)
for temp in bList:
    if int(temp) > h:
        result += 1
print(result)