tempList = input().split()
cri = int(tempList[1])
strList = input().split()
result = 0
for var in strList:
    i = 0
    temp = 0
    while i < len(var):
        if var[i] == '4' or var[i] == '7':
            temp += 1
        i += 1
    if temp <= cri:
        result += 1
print(result)