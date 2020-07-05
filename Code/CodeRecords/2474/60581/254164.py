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

while count < testNumber:
    stringList = input[start].copy()
    stack = []
    i = 0
    maxLength = 0
    length = 0
    while i < len(stringList):
        if stringList[i] == '(':
            stack.append('(')
        elif stringList[i] == ')':
            if len(stack) == 0:
                stack.append(')')
                i += 1
                continue
            if stack[len(stack)-1]=='(':
                stack.remove(stack[len(stack)-1])
                length += 2
            else:
                if length > maxLength:
                    maxLength = length
                stack.append(')')
                length = 0
        i += 1
    if length > maxLength:
        maxLength = length
    print(maxLength)



    count += 1
    start += 1
