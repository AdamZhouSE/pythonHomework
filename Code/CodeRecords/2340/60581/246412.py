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
    blocks = input[start][0]
    blockHeights = input[start+1].copy()
    begin = 0
    end = blocks - 1
    if blocks < 3:
        print("0")
    else:
        for i in range(1,blocks):
            if blockHeights[i] >= blockHeights[begin]:
                begin = i
            else:
                break
        for i in range(1,blocks):
            if blockHeights[blocks-i] >= blockHeights[end]:
                end = i
            else:
                break
        if begin >= end:
            print("0")
        else:
            height = min(blockHeights[begin],blockHeights[end])
            contain = 0
            for i in range(begin+1,end):
                contain += height - blockHeights[i]
            print(contain)
    start += 2
    count += 1