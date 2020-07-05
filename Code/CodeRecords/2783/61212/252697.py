num = int(input())
dic = []


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
    else:
        element1 = dic[contain(tempList[0], dic)]
        if element[1]<=0:
            element = [tempList[0], element[1] + element1[1]]
            dic.remove(element1)
            dic.append(element)
        else:
            element = [tempList[0], element[1] + element1[1]]
            dic[contain(tempList[0], dic)]=element
            
res = dic[0]
for el in dic:
    if res[1] < el[1]:
        res = el

print(res[0])
