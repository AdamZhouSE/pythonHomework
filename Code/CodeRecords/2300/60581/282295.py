lst = []
line = "0"
while line != "":
    try:
        line = input()
        lst.append(line)
    except:
        lst.append(line)
        break
lst.remove(lst[-1])
input = []
#读入处理
for i in range(0,len(lst)):
    theLine = []
    j = 0
    while j < len(lst[i]):
        str = ''
        judgeWord = False
        judgeNumber = False
        if (lst[i][j]>='A' and lst[i][j]<='Z') or (lst[i][j]>='a' and lst[i][j]<='z') or lst[i][j]=='#':
            judgeWord = True
            str += lst[i][j]
            theLine.append(str)
        j += 1
    input.append(theLine)

thelist = input[0]
numberList = []
count = 0

for i in range(len(thelist)):
    if thelist[i]!='#':
        numberList.insert(count,thelist[i])
    else:
        count += 1

for i in range(len(numberList)):
    if i >= 7:
        break
    print(numberList[i],end=" ")




