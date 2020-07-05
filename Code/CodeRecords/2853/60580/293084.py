size = int(input())
tempList = input().split()
intList = []
for var in tempList:
    intList.append(int(var))
all = 0
for var in intList:
    all += var
result = 0
if all % 2 == 0:
    for i in intList:
        if i % 2 == 0:
            result += 1
    print(result)
else:
    for i in intList:
        if i % 2 == 1:
            result += 1
    print(result)