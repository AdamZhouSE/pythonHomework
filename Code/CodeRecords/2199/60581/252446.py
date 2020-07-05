import sys

lst = []
for line in sys.stdin:
    if line.strip()=="":
        break
    lst.append(line)

def findMaxString(wordList):
    length = len(wordList)
    stringList = []
    for i in range(length):
        for j in range(i,length+1):
            judge = False
            for h in range(len(stringList)):
                if stringList[h][0]==wordList[i:j]:
                    judge = True
                    stringList[h][1] += 1
                    break
            if not judge:
                stringList.append([wordList[i:j],1])
    i = 0
    while i < len(stringList):
        if stringList[i][1]<=1:
            stringList.remove(stringList[i])
        else:
            i += 1

    if len(stringList)==0:
        return []
    maxLength = 0
    point = 0
    for h in range(len(stringList)):
        if len(stringList[h][0])>maxLength:
            maxLength = len(stringList[h][0])
            point = h

    return  stringList[point][0]



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

string = input[0].copy()

count = 0
while len(string)>0:
    count += 1
    string = findMaxString(string)

print(count)