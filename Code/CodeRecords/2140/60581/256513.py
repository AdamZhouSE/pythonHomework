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
def move(string):
    storage = string[0]
    string = string[1:]
    string.append(storage)
    return string


count = 0
start = 1

while count < testNumber:
    num = input[start][0]
    stringList = [0]*num
    moveTime = 0
    for i in range(1,num+1):
        totalCount = 0
        while totalCount < i:
            if stringList[0] != 0:
                stringList = move(stringList)
                moveTime += 1
            else:
                stringList = move(stringList)
                moveTime += 1
                totalCount += 1
        while stringList[0] != 0:
            stringList = move(stringList)
            moveTime += 1
        stringList[0] = i
    moveTime = moveTime%num
    while moveTime < num:
        stringList = move(stringList)
        moveTime += 1
    for i in range(num-1):
        print(stringList[i],end=" ")
    print(stringList[-1])

    count += 1
    start += 1
