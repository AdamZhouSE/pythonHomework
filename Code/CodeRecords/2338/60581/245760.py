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
        judgeNumber = False
        if lst[i][j]>='0' and lst[i][j]<='9':
            judgeNumber = True
            str += lst[i][j]
        while judgeNumber:
            j += 1
            if j == len(lst[i])-1:
                if lst[i][j] >= '0' and lst[i][j] <= '9':
                    str += lst[i][j]
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
start = 1
count = 0
while count < testNumber:
    numbers = input[start][0]
    total = input[start][1]
    numberList = input[start+1].copy()
    judge = False
    for i in range(0,numbers-1):
        for j in range(1,numbers):
            if total == numberList[i]+numberList[j]:
                judge = True
    if judge:
        print("Yes")
    else:
        print("No")

    
    count += 1
    start += 2
