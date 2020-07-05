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
            theLine.append(int(str))
        j += 1
    input.append(theLine)

stringList = input[0].copy()
numberList = input[1].copy()
k = input[2][0]

goodWord = []
badWord = []

length = len(stringList)
for i in range(length):
    if numberList[i]==0:
        if badWord.count(stringList[i])==0:
            badWord.append(stringList[i])
    else:
        if goodWord.count(stringList[i])==0:
            goodWord.append(stringList[i])

count = 0
subStringList = []
for i in range(0,length):
    for j in range(1,length+1):
        subString = stringList[i:j].copy()
        judge = False
        for h in range(len(subStringList)):
            if subString == subStringList[h]:
                judge = True
                break
        if not judge:
            subStringList.append(subString)

for i in range(len(subStringList)):
    badNumber = 0
    for j in range(len(badWord)):
        badNumber += subStringList[i].count(badWord[j])
    if badNumber <= k:
        count += 1

print(count-1)