# 可以用元组、二维数组、字典
# 先进行排序
string = input()
overallList = []
couple = []


def indexDel(index):
    global string
    listTemp = list(string)
    del listTemp[index]
    string = ''.join(listTemp)


count = 0
while len(string) > 0:
    character = string[0]
    couple.append(character)

    i = 0
    while i < len(string):
        if string[i] == character:
            count += 1
            indexDel(i)
            i -= 1
        i += 1
    couple.append(count)
    overallList.append(couple)
    count = 0
    couple = []


def sortKey(elem):
    return elem[1]


overallList.sort(key=sortKey,reverse=True)
for elem in overallList:
    print(elem[0]*elem[1],end='')
print()