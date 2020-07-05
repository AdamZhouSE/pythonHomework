def merge(aList, bList):
    res = []
    i, j = 0, 0
    a, b = len(aList), len(bList)
    while i < a and j < b:
        if aList[i] < bList[j]:
            res.append(aList[i])
            i += 1
        else:
            res.append(bList[j])
            j += 1
    while i < a:
        res.append(aList[i])
        i += 1
    while j < b:
        res.append(bList[j])
        j += 1
    return res


listList = input().strip('[|]').split('],[')
listList = [[int(i) for i in j.split(',')] for j in listList]  # 视为双端队列
while len(listList) != 1:
    listList.append(merge(listList[0], listList[1]))
    listList.pop(0)
    listList.pop(0)
print(listList[0], end='\n')
