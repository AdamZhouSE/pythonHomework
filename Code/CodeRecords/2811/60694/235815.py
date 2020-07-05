x = input()
xList = x.split(" ")

p = int(xList[0])
num = int(xList[1])

aList = []
for i in range(num):
    aList.append(int(input()))

aSet = set()
flag = 0
for ele in aList:
    position = ele % p
    preLen = len(aSet)
    aSet.add(position)
    afterLen = len(aSet)
    if preLen == afterLen:
        print(preLen + 1)
        flag = 1
        break

if flag == 0:
    print(-1)
