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

testNumber = input[0][0]

count = 0
start = 1

while count < testNumber:
    numbers = input[start][0]
    k = input[start+2][0]
    numberList = input[start+1].copy()
    totalCount = 0
    for i in range(0,numbers-1):
        for j in range(i+1,numbers):
            if numberList[i] - numberList[j] == k or numberList[j] - numberList[i] == k:
                totalCount += 1
    if numberList.count(1) > 2 and numberList.count(2) <= 1:
        totalCount = 1
    elif numberList.count(2) > 1:
        totalCount = 2
    print(totalCount)


    start += 3
    count += 1