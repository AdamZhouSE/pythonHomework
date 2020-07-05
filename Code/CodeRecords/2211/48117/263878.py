nk = input().split(' ')
n = int(nk[0])
k = int(nk[1])

nameList = []

for i in range(n):
    name_num = input().split(' ')
    name = name_num[0]
    num = int(name_num[1])
    nameList.append((name, num))

nameList = sorted(nameList, key=lambda x: x[1], reverse=True)
nameStr = ''

for name in nameList:
    nameStr += name[0]

for j in range(k):
    interestedName = (input())
    print(nameStr.count(interestedName))