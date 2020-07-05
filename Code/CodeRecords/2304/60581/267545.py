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

theList = input[1:]
maxNum = len(theList)

def getNextLever(lever):
    nextLever = []
    length = len(lever)
    for i in range(length):
        for j in range(maxNum):
            if lever[i] == theList[j][0]:
                if theList[j][1] != 0:
                    nextLever.append(theList[j][1])
                if theList[j][2] != 0:
                    nextLever.append(theList[j][2])
    return nextLever

allInTheTree = 1
allLevers = []
thisLever = []
for i in range(maxNum):
    if root == theList[i][0]:
        thisLever.append(theList[i][0])

allLevers.append(thisLever)

while allInTheTree < maxNum:
    nextLever = getNextLever(thisLever)
    allInTheTree += len(nextLever)
    allLevers.append(nextLever)
    thisLever = nextLever

for i in range(len(allLevers)):
    print('Level',end=" ")
    print(i+1,end=" : ")
    for j in range(len(allLevers[i])):
        if j == len(allLevers[i]) - 1:
            print(allLevers[i][j])
        else:
            print(allLevers[i][j], end=" ")

for i in range(len(allLevers)):
    print('Level',end=" ")
    print(i+1,end=" ")
    if i % 2 == 0:
        print('from left to right: ', end='')
    else:
        print('from right to left: ', end='')
        allLevers[i].reverse()
    for j in range(len(allLevers[i])):
        if j == len(allLevers[i])-1:
            print(allLevers[i][j])
        else:
            print(allLevers[i][j],end=" ")






