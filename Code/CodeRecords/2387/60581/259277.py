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

listNumber = input[0][0]
functionNum = input[0][1]

wordList = input[1]

method = input[2:2+functionNum]

outPutPlace = input[2+functionNum][0]

for i in range(len(method)):
    if method[i][0] == 0:
        judge = True
    else:
        judge = False
    startNum = method[i][1]-1
    endNum = method[i][2]
    subString = wordList[startNum:endNum]
    subString.sort()
    if not judge:
        subString.reverse()
    wordList[startNum:endNum] = subString

print(wordList[outPutPlace-1])