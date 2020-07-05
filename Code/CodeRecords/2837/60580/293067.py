temp = input().split()
num = int(temp[0])
l = int(temp[1])
r = int(temp[2])
if num == 1:
    print("1 1")
else:
    min = 0
    temp = 1
    i = 0
    minList = []
    while i < l:
        minList.append(temp)
        temp *= 2
        i += 1
    for var in minList:
        min += var
    min += num - l
    max = 0
    temp = 1
    i = 0
    maxList = []
    while i < r:
        maxList.append(temp)
        temp *= 2
        i += 1
    for var in maxList:
        max += var
    max += (num - r) * maxList[len(maxList) - 1]
    print(str(min) + " " + str(max))