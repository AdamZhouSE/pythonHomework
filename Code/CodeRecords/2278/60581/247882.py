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

testNumber = input[0][0]

def XOR(numberA,numberB):
    lstA = []
    lstB = []
    while numberA > 0:
        if numberA%2==1:
            lstA.append(1)
        else:
            lstA.append(0)
        numberA = int(numberA/2)
    while numberB > 0:
        if numberB%2==1:
            lstB.append(1)
        else:
            lstB.append(0)
        numberB = int(numberB/2)
    while len(lstA) < len(lstB):
        lstA.append(0)
    while len(lstB) < len(lstA):
        lstB.append(0)

    outPut = []
    for i in range(len(lstA)):
        if lstA[i]==lstB[i]:
            outPut.append(0)
        else:
            outPut.append(1)
    numberReturn = 0
    outPut.reverse()
    for i in range(len(outPut)):
        numberReturn = numberReturn*2+outPut[i]
    return numberReturn


start = 1
count = 0
while count < testNumber:
    number = input[start][0]
    numberList = input[start+1].copy()
    outPut = []
    for i in range(number-1):
        outPut.append(XOR(numberList[i],numberList[i+1]))
    outPut.append(numberList[number-1])
    for i in range(number):
        print(outPut[i],end=" ")
    print()
    start += 2
    count += 1