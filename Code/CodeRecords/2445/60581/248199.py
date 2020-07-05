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


stringS = input[0][1]
stringT = input[0][3]

splitS = []
for i in range(len(stringS)):
    splitS.append(stringS[i])
splitT = []
for i in range(len(stringT)):
    splitT.append(stringT[i])

if len(splitS)!=len(stringT):
    print("false")
else:
    judge = True
    while len(splitS) != 0:
        if splitT.count(splitS[0]):
            splitT.remove(splitS[0])
            splitS.remove(splitS[0])
        else:
            judge = False
            break
    if judge:
        print("true")
    else:
        print("false")

print(splitS)
print(stringT)

