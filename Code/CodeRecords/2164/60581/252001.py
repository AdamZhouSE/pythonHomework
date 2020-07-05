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

start = 1
count = 0

while count < testNumber:
    numberList = input[start][0]
    wordList = []
    for i in range(len(numberList)):
        judge = False
        for j in range(len(wordList)):
            if numberList[i] == wordList[j]:
                judge = True
                break
        if not judge:
            wordList.append(numberList[i])
    print(len(numberList)-len(wordList))
    
    count += 1
    start += 1