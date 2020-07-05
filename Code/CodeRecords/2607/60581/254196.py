lst = []
line = "0"
while line != "":
    try:
        line = input()
        lst.append(line)
    except:
        lst.append(line)
        break
lst.remove(lst[-1])
input = []
#读入处理
for i in range(0,len(lst)):
    theLine = []
    j = 0
    while j < len(lst[i]):
        str = ''
        judgeWord = False
        judgeNumber = False
        if lst[i][j]>='0' and lst[i][j]<='9':
            judgeNumber = True
            str += lst[i][j]
        while judgeNumber:
            j += 1
            if j == len(lst[i]):
                theLine.append(str)
                break
            if lst[i][j]>='0' and lst[i][j]<='9':
                str += lst[i][j]
            else:
                judgeNumber = False
                theLine.append(str)
        j += 1
    input.append(theLine)

testNumber = int(input[0][0])

count = 0
start = 1
while count < testNumber:
    stringList = input[start][0]
    stringSplit = []
    for i in range(len(stringList)):
        stringSplit.append(stringList[i])
    totalCount = 0
    for i in range(0,len(stringSplit)):
        for j in range(1,len(stringSplit)+1):
            stringCopy = stringSplit[i:j].copy()
            if stringCopy.count('1')==stringCopy.count('2') and stringCopy.count('2')==stringCopy.count('0') and stringCopy.count('1')!=0:
                totalCount += 1
    print(totalCount)
    start += 1
    count += 1