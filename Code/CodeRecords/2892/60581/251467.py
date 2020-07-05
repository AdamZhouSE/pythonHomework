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
        while judgeWord:
            j += 1
            if j == len(lst[i]):
                theLine.append(str)
                break
            if (lst[i][j]>='A' and lst[i][j]<='Z') or (lst[i][j]>='a' and lst[i][j]<='z'):
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

startNum = input[0][0]
endNum = input[0][1]+1

countNumber = [0]*10

for num in range(startNum,endNum):
    stringNum = []
    storage = num
    while num > 0:
        stringNum.insert(0,num%10)
        num = int(num/10)
    countNumber[0] += stringNum.count(0)
    countNumber[1] += stringNum.count(1)
    countNumber[2] += stringNum.count(2)
    countNumber[3] += stringNum.count(3)
    countNumber[4] += stringNum.count(4)
    countNumber[5] += stringNum.count(5)
    countNumber[6] += stringNum.count(6)
    countNumber[7] += stringNum.count(7)
    countNumber[8] += stringNum.count(8)
    countNumber[9] += stringNum.count(9)

for i in range(len(countNumber)):
    if i == len(countNumber)-1:
        print(countNumber[i],end="")
    else:
        print(countNumber[i],end=" ")

