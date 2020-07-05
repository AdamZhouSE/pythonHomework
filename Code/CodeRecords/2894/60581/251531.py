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
string = input[1].copy()

countVK = 0
i = 0
leftList = []
while len(string)>0:
    if string[i]=='V' and string[i+1] == 'K':
        countVK += 1
        if i > 0:
            before = string[0:i].copy()
            leftList.append(before)
            string = string[i+2:]
            i = 0
        else:
            string = string[i+2:]
    elif i == len(string)-1:
        leftList.append(string)
        break
    else:
        i += 1

judge = False
for i in range(len(leftList)):
    if len(leftList[i]) >= 3:
        judge = True
        break
    elif len(leftList[i])==2:
        if leftList[i]==['K','K'] or leftList[i]==['V','V']:
            judge = True
            break
if judge:
    countVK += 1

print(countVK,end="")