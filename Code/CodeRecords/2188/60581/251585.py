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

stringLength = input[0][0]

numberK = input[0][1]
stringA = input[1].copy()
stringB = input[2].copy()

testNumber = input[3][0]

count = 0
start = 4
while count < testNumber:
    darkBonus = input[start][0]-1
    benefits = 0
    stringT = stringA[input[start][0]-1:input[start][1]]
    stringP = stringB[input[start][2]-1:input[start][3]]
    lenT = len(stringT)
    lenP = len(stringP)
    for i in range(lenT-lenP+1):
        judge = True
        for j in range(lenP):
            if stringT[i+j]!=stringP[j]:
                judge = False
                break
        if judge:
            for h in range(lenP):
                stringT[i+h] = 0
            benefits += numberK - i - 1 - darkBonus
    print(benefits)
    count += 1
    start += 1

