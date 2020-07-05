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

numberList = input[0].copy()

numberList.sort()
odd = []
even = []

for i in range(len(numberList)):
    if numberList[i]%2==1:
        odd.append(numberList[i])
    else:
        even.append(numberList[i])

outPut = []
for i in range(len(odd)):
    outPut.append(even[i])
    outPut.append(odd[i])

print(outPut)