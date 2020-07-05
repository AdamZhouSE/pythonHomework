def sortKey(elem):
    return elem[1]


stringList = input().split()
stringList.sort()
imformation = []
couple = []

while len(stringList) > 0:
    tempCmp = stringList[0]
    index = 0
    count = 0
    while index < len(stringList):
        if stringList[index] == tempCmp:
            count += 1
            del stringList[index]
            index -= 1
        index += 1
    couple = [tempCmp, count]
    imformation.append(couple)
imformation.sort(key=sortKey, reverse=True)
print(str(imformation[0][0]) + ' ' + str(imformation[0][1]))
