n = int(input())
socks = [int(i) for i in input().split(" ")]
onTable = []
maxNum = 0
for i in socks:
    if onTable.count(i) == 0:
        onTable.append(i)
        if len(onTable)>=maxNum:
            maxNum = len(onTable)
    else:
        onTable.remove(i)
print(maxNum)