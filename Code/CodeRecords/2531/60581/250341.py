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
        if (lst[i][j]>='A' and lst[i][j]<='Z') or (lst[i][j]>='a' and lst[i][j]<='z'):
            str += lst[i][j]
            theLine.append(str)
        j += 1
    input.append(theLine)

stringList = input[0].copy()

wordList = []
while len(stringList) > 0:
    storage = stringList[0]
    number = stringList.count(storage)
    wordList.append([number,storage])
    while stringList.count(storage) > 0:
        stringList.remove(storage)

while len(wordList) > 0:
    maxNumber = 0
    maxPoint = 0
    for i in range(0,len(wordList)):
        if wordList[i][0] > maxNumber:
            maxNumber = wordList[i][0]
            maxPoint = i
    for i in range(maxNumber):
        print(wordList[maxPoint][1],end="")
    wordList.remove(wordList[maxPoint])
        
