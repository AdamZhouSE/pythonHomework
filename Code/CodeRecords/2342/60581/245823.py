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
            if j == len(lst[i]):
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
start = 1
count = 0
while count < testNumber:
    words = input[start][0]
    reverseNumber = input[start][1]
    numberList = input[start+1].copy()
    subStart = 0
    subCount = 0
    totalNumber = int(words/reverseNumber)
    if words%reverseNumber != 0:
        totalNumber += 1
    while subCount < totalNumber:
        subString = numberList[subStart:subStart+reverseNumber].copy()
        subString.reverse()
        numberList[subStart:subStart+reverseNumber] = subString.copy()
        subCount += 1
        subStart += reverseNumber
    #输出
    for i in range(0,len(numberList)):
        if i == len(numberList)-1:
            if count + 1 == testNumber:
                print(numberList[i],end="")
            else:
                print(numberList[i])
        else:
            print(numberList[i],end=" ")

    start += 2
    count += 1