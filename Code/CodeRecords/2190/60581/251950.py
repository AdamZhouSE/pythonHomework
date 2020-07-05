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
        if (lst[i][j]>='A' and lst[i][j]<='Z') or (lst[i][j]>='a' and lst[i][j]<='z'):
            judgeWord = True
            str += lst[i][j]
            theLine.append(str)

        if lst[i][j]>='0' and lst[i][j]<='9':
            judgeNumber = True
            str += lst[i][j]
        while judgeNumber:
            j += 1
            if j == len(lst[i]):
                theLine.append(int(str))
                break
            if lst[i][j]>='0' and lst[i][j]<='9':
                str += lst[i][j]
            else:
                judgeNumber = False
                theLine.append(int(str))
        j += 1
    input.append(theLine)

testNumber = input[0][0]

count = 0
start = 1

while count < testNumber:
    existNumber = input[start][-1]
    stringList = input[start][0:len(input[start])-1].copy()
    numberList = [[0,0]]
    stringNumber = 1
    while stringNumber <= len(stringList):
        for i in range(len(stringList)-stringNumber+1):
            subString = stringList[i:i+stringNumber].copy()
            judge = False
            for j in range(len(numberList)):
                if subString == numberList[j][0]:
                    judge = True
                    numberList[j][1] += 1
            if not judge:
                numberList.append([subString,1])
        stringNumber += 1
    i = 0
    while i < len(numberList):
        if numberList[i][1] != existNumber:
            numberList.remove(numberList[i])
        else:
            i += 1
    if len(numberList)==0:
        print("-1")
    else:
        maxLength = 1
        for i in range(len(numberList)):
            if len(numberList[i][0]) > maxLength:
                maxLength = len(numberList[i][0])

        lengthNumber = [0]*maxLength
        for i in range(len(numberList)):
            lengthNumber[len(numberList[i][0])-1] += 1

        point = 0
        maxN = 0
    
        for i in range(len(lengthNumber)):
            if lengthNumber[i]>=maxN:
                maxN = lengthNumber[i]
                point = i
        print(point+1)



    count += 1
    start += 1