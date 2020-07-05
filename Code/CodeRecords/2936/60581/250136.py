import sys

lst = []
for line in sys.stdin:
    if line.strip()=="":
        break
    lst.append(line)

input = []
#读入处理
for i in range(0,len(lst)):
    theLine = []
    j = 0
    while j < len(lst[i]):
        str = ''
        if (lst[i][j]>='A' and lst[i][j]<='Z') or (lst[i][j]>='0' and lst[i][j]<='9') or lst[i][j]=='-':
            str += lst[i][j]
            theLine.append(str)
        j += 1
    input.append(theLine)

stringNumber = input[0][0]
stringList = input[1:].copy()
stringList.sort()
storage = stringList.copy()
for i in range(len(storage)):
    storage[i] = "".join(storage[i])
for i in range(len(stringList)):
    while stringList[i].count('-'):
        stringList[i].remove('-')
    for j in range(len(stringList[i])):
        if stringList[i][j] == 'A' or stringList[i][j] == 'B' or stringList[i][j] == 'C':
            stringList[i][j] = '2'
        elif stringList[i][j] == 'D' or stringList[i][j] == 'E' or stringList[i][j] == 'F':
            stringList[i][j] = '3'
        elif stringList[i][j] == 'G' or stringList[i][j] == 'H' or stringList[i][j] == 'I':
            stringList[i][j] = '4'
        elif stringList[i][j] == 'J' or stringList[i][j] == 'K' or stringList[i][j] == 'L':
            stringList[i][j] = '5'
        elif stringList[i][j] == 'M' or stringList[i][j] == 'N' or stringList[i][j] == 'O':
            stringList[i][j] = '6'
        elif stringList[i][j] == 'P' or stringList[i][j] == 'R' or stringList[i][j] == 'S':
            stringList[i][j] = '7'
        elif stringList[i][j] == 'T' or stringList[i][j] == 'U' or stringList[i][j] == 'V':
            stringList[i][j] = '8'
        elif stringList[i][j] == 'W' or stringList[i][j] == 'X' or stringList[i][j] == 'Y':
            stringList[i][j] = '9'

for i in range(len(stringList)):
    stringList[i] = "".join(stringList[i])

judge = False
i = 0
while i < len(stringList):
    if stringList.count(stringList[i])>1:
        judge = True
        print(storage[i],end=" ")
        print(stringList.count(stringList[i]))
        store = stringList[i]
        while stringList.count(store) > 0:
            if stringList.count(store) == 1:
                stringList.remove(store)
                break
            stringList.remove(store)
    else:
        i += 1

if not judge:
    print("No duplicates.",end=" ")
