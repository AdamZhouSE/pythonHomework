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
    maxLength = 0
    for i in range(len(stringList)-1):
        length = 0
        if stringList[i]=='(' and stringList[i+1]==')':
            length = 2
            storage = i + 2
            judge = True
            while storage < len(stringList)-1:
                if stringList[storage]=='(' and stringList[storage+1]==')':
                    length += 2
                    storage += 2
                else:
                    judge = False
                    break
        if length > maxLength:
            maxLength = length
    print(maxLength)

    count += 1
    start += 1
print(input)