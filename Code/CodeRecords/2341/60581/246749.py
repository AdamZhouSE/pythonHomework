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
    lengthN = input[start][0]
    lengthM = input[start][1]
    N = input[start+1].copy()
    N.sort()
    M = input[start+2].copy()
    M.sort()
    numberN = 0
    numberM = 0
    totalSort = []
    while numberN<lengthN or numberM<lengthM:
        if N[numberN]<=M[numberM]:
            totalSort.append(N[numberN])
            numberN += 1
        else:
            totalSort.append(M[numberM])
            numberM += 1
    N = totalSort[0:lengthN]
    M = totalSort[lengthN:]
    for i in range(len(totalSort)):
        print(totalSort[i],end=" ")
        if i == len(totalSort)-1:
            print()
    start += 3
    count += 1