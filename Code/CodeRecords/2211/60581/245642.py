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
        judgeWord = False
        judgeNumber = False
        if lst[i][j]>='A' and lst[i][j]<='Z':
            judgeWord = True
            str += lst[i][j]
        while judgeWord:
            j += 1
            if j == len(lst[i])-1:
                theLine.append(str)
                break
            if lst[i][j]>='A' and lst[i][j]<='Z':
                str += lst[i][j]
            else:
                judgeWord = False
                theLine.append(str)

        if lst[i][j]>='0' and lst[i][j]<='9':
            judgeNumber = True
            str += lst[i][j]
        while judgeNumber:
            j += 1
            if j == len(lst[i])-1:
                theLine.append(int(str))
                break
            if lst[i][j]>='0' and lst[i][j]<='9':
                str += lst[i][j]
            else:
                judgeNumber = False
                theLine.append(int(str))
        j += 1
    input.append(theLine)

queenNumber = input[0][0]
stringNumber = input[0][1]

queenList = input[1:queenNumber+1]
stringList = input[queenNumber+1:1+queenNumber+stringNumber]

queenName = [0]*queenNumber

while queenName.count(0)!=0:
    for i in range(queenNumber):
        if queenList[i][1] == 0:
            queenName[i] = queenList[i][0]
        else:
            if queenName[queenList[i][1]-1] != 0:
                queenName[i] = queenList[i][0] +queenName[queenList[i][1]-1]

for i in range(stringNumber):
    count = 0
    for j in range(queenNumber):
        forehead = queenName[j][0:len(stringList[i][0])]
        if forehead == stringList[i][0]:
            count += 1
    print(count)



