nk = input().split(' ')
n = int(nk[0])
k = int(nk[1])

nameDict = dict()

for i in range(n):
    name_num = input().split(' ')
    name = name_num[0]
    num = int(name_num[1])
    nameDict[name] = num

nameDict = sorted(nameDict.items(), key=lambda x: x[1], reverse=True)
nameStr = ''
for t in nameDict:
    nameStr += t[0]


for j in range(k):
    interestedName = (input())
    print(nameStr.count(interestedName))