import re
ori = input()
infos = re.sub(r'\W+', " ", ori).strip().split(" ")
index = 0
allRest = []
while index < len(infos):
    aRest = []
    for i in range(5):
        aRest.append(int(infos[index+i]))
    allRest.append(aRest)
    index += 5
filteredRes = []
vegi = int(input())
price = int(input())
dis = int(input())
for r in allRest:
    if r[2] == vegi and r[3] <= price and r[4] <= dis:
        filteredRes.append(r)
l = len(filteredRes)
while l > 1:
    for i in range(l-1):
        if filteredRes[i][1] > filteredRes[i+1][1]:
            temp = filteredRes[i+1]
            filteredRes[i+1] = filteredRes[i]
            filteredRes[i] = temp
    l -= 1
idList = []
j = len(filteredRes) - 1
while j >= 0:
    idList.append(filteredRes[j][0])
    j -= 1
print(idList)