num = int(input())
dic = []
record=[]

def contain(element, lists):
    for x in lists:
        if x[0] == element:
            return lists.index(x)
    return -1


for i in range(0, num):
    tempList = list(input().split(" "))
    element = [tempList[0], int(tempList[1])]
    if contain(tempList[0], dic) == -1:
        dic.append(element)
        record.append(element)
    else:
        element1 = dic[contain(tempList[0], dic)]
        element = [tempList[0], element[1] + element1[1]]
        record.append(element)
        dic.remove(element1)
        dic.append(element)

res = dic[0]
multipleMax=False
for el in dic:
    if res[1] < el[1]:
        res = el

for el in dic:
    if res[1]==el[1] and res!=el:
        multipleMax=True

if multipleMax:
    for el in record:
        if res[1]<=el[1]:
            res=el
            break

print(res[0])
