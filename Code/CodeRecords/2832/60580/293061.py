size = int(input())
tempList = input().split()
pageList = []
pageList.append(0)
for var in tempList:
    pageList.append(int(var))
i = 1
result = 0
while i < len(pageList):
    l = []
    l.append(pageList[i])
    l.sort()
    while i < l[len(l) - 1]:
        i += 1
        l.append(pageList[i])
        l.sort()
    result += 1
    i += 1
print(result)