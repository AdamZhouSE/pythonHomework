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
            while judgeWord:
                if j + 1 == len(lst[i]):
                    theLine.append(str)
                    break
                if (lst[i][j+1] >= 'A' and lst[i][j+1] <= 'Z') or (lst[i][j+1] >= 'a' and lst[i][j+1] <= 'z'):
                    str += lst[i][j+1]
                    j += 1
                else:
                    judgeWord = False
                    theLine.append(str)


        elif lst[i][j] == '+' or  lst[i][j] == '-' or  lst[i][j] == '*' or  lst[i][j] == '/' or \
                    lst[i][j] == '(' or lst[i][j] == ')' or lst[i][j] == '^':
            str += lst[i][j]
            theLine.append(str)


        elif lst[i][j]>='0' and lst[i][j]<='9':
            judgeNumber = True
            str += lst[i][j]
            while judgeNumber:
                if j + 1 == len(lst[i]):
                    theLine.append(int(str))
                    break
                if lst[i][j+1] >= '0' and lst[i][j+1] <= '9':
                    str += lst[i][j+1]
                    j += 1
                else:
                    judgeNumber = False
                    theLine.append(int(str))
        j += 1
    input.append(theLine)

n = input[0][0]
root = input[0][1]
node = input[len(input)-1][0]

theList = input[1:len(input)-1]
maxNum = len(theList)
theMaxNumber = 0
for i in range(len(theList)):
    if theList[i][0]>theMaxNumber:
        theMaxNumber = theList[i][0]

def getLCH(num):
    for i in range(maxNum):
        if num == theList[i][0]:
            return theList[i][1]
    return 0

def getRCH(num):
    for i in range(maxNum):
        if num == theList[i][0]:
            return theList[i][2]
    return 0

def getFa(num):
    for i in range(maxNum):
        if num == theList[i][1] or num == theList[i][2]:
            return theList[i][0]
    return 0

read = []
visited = [0]*theMaxNumber
now = root
while len(read) < maxNum:
    itsLeft = getLCH(now)
    itsRight = getRCH(now)
    itsFa = getFa(now)
    if itsLeft != 0 and visited[itsLeft-1] == 0:
        now = itsLeft
    elif itsLeft == 0 and visited[now-1] == 0:
        read.append(now)
        visited[now-1] = 1
        if itsRight != 0 and visited[itsRight-1] == 0:
            now = itsRight
    elif itsRight != 0 and visited[itsRight-1] == 0:
        read.append(now)
        visited[now - 1] = 1
        now = itsRight
    else:
        if visited[now-1] == 0:
            read.append(now)
            visited[now-1] = 1
            now = itsFa
        else:
            now = itsFa

place = maxNum
for i in range(maxNum):
    if node == read[i]:
        place = i + 1

if place >= maxNum:
    print(0)
else:
    print(read[place])