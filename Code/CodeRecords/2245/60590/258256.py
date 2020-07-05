num = int(input())
binStr = bin(num)
#print(binStr)
arr = list(binStr)

onesIndex = []
for i in range(2, arr.__len__()):
    if arr[i] == '1':
        onesIndex.append(i)
#print(onesIndex)

if onesIndex.__len__() == 1:
    print(0)
else:
    res = []
    for i in range(onesIndex.__len__() - 1):
        temp = int(onesIndex[i + 1]) - int(onesIndex[i])
        res.append(temp)
    print(max(res))