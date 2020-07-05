a = int(input())
tempList = input().split()
intList = []
for var in tempList:
    intList.append(int(var))
d = {}
for var in intList:
    if var in d.keys():
        d[var] += 1
    else:
        d[var] = 1
l = sorted(d.keys())
realD = {}
for i in l:
    realD[i] = d[i]
resultD = {}
resultD[0] = 0
resultD[1] = 0
for i in l:
    if i % 2 == 0:
        resultD[0] += realD[i]
    else:
        resultD[1] += realD[i]
if resultD[0] >= resultD[1]:
    print(resultD[1])
else:
    print(resultD[0])
