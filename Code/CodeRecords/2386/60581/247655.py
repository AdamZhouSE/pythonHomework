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
        if lst[i][j]>='A' and lst[i][j]<='Z':
            judgeWord = True
            str += lst[i][j]
        while judgeWord:
            j += 1
            if j == len(lst[i]):
                theLine.append(str)
                break
            if lst[i][j]>='A' and lst[i][j]<='Z':
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

testNumber = input[0][0]

start = 1
count = 0
while count < testNumber:
    number = input[start][0]
    numberList = input[start+1].copy()
    addTo = input[start+2][0]
    if number < 4:
        print("0")
    elif number == 4:
        if addTo == numberList[0]+numberList[1]+numberList[2]+numberList[3]:
            print("1")
        else:
            print("0")
    else:
        judge = False
        for i in range(0,number-3):
            for j in range(i+1,number-2):
                for h in range(j+1,number-1):
                    for l in range(h+1,number):
                        if addTo == numberList[i]+numberList[j]+numberList[h]+numberList[l]:
                            print("1")
                            judge = True
                            break
                    if judge:
                        break
                if judge:
                    break
            if judge:
                break
        if not judge:
            print("0")

    start += 3
    count += 1