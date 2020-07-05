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
length = len(stringList)

for i in range(length):
    if numberList[i] == 1:
        numberList[i] = 0
    else:
        numberList[i] = 1

count = 0
subStringList = []
for i in range(0,length):
    for j in range(i+1,length+1):
        badNumber = 0
        subString = stringList[i:j].copy()
        for h in range(i,j):
            badNumber += numberList[h]
        pair = [subString,badNumber]
        judge = False
        for h in range(len(subStringList)):
            if pair == subStringList[h]:
                judge = True
                break
        if not judge:
            subStringList.append(pair)

start = 0
point = 1
while start < len(subStringList):
    while point < len(subStringList):
        if subStringList[start][0] == subStringList[point][0]:
            subStringList.remove(subStringList[point])
        else:
            point += 1
    start += 1
    point = start + 1


for i in range(len(subStringList)):
    if subStringList[i][1]<=k:
        count += 1
print(count)
