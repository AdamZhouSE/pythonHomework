m = eval(input())
ms = [int(x) for x in input().split()]
res = []
n = eval(input())
for i in range(n):
    left, right = [int(x) for x in input().split()]
    tempLst = []
    for j in range(left - 1,right):
        if ms[j] not in tempLst:
            tempLst.append(ms[j])
    print(len(tempLst))
    res.append(len(tempLst))
#print(*res)