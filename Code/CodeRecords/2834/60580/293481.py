a = input().split()
peopleNum = int(a[0])
questionNum = int(a[1])
strL = []
for i in range(peopleNum):
    strL.append(input())
tempList = input().split()
scoreNum = []
for var in tempList:
    scoreNum.append(int(var))
j = 0
result = 0
while j < questionNum:
    k = 0
    d = {}
    while k < peopleNum:
        if strL[k][j] not in d.keys():
            d[strL[k][j]] = 1
        else:
            d[strL[k][j]] += 1
        k += 1
    t = sorted(d.items(), key=lambda item: item[1], reverse=True)
    result += t[0][1] * scoreNum[j]
    j += 1
print(result)
