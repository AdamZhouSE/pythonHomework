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
        if lst[i][j]>='(' and lst[i][j]<=')':
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

while count < testNumber :
    theList = input[start].copy()
    stack = []
    bracketsCount = 0
    for i in range(len(theList)):
        if theList[i] == '(':
            bracketsCount += 1
            stack.append(['(',bracketsCount])
            print(bracketsCount,end=" ")
        elif theList[i] == ')':
            if len(stack) > 0:
                thisCount = stack[len(stack)-1][1]
                print(thisCount,end=" ")
                stack.remove(stack[len(stack)-1])
    print()
    count += 1
    start += 1