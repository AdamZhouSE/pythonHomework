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

def translate(string):
    for i in range(len(string)):
        if string[i] == 'A':
            string[i] = 1
        elif string[i] == 'B':
            string[i] = 2
        elif string[i] == 'C':
            string[i] = 3
        elif string[i] == 'D':
            string[i] = 4
        elif string[i] == 'E':
            string[i] = 5
        elif string[i] == 'F':
            string[i] = 6
        elif string[i] == 'G':
            string[i] = 7
        elif string[i] == 'H':
            string[i] = 8
        elif string[i] == 'I':
            string[i] = 9
        elif string[i] == 'J':
            string[i] = 10
        elif string[i] == 'K':
            string[i] = 11
        elif string[i] == 'L':
            string[i] = 12
        elif string[i] == 'M':
            string[i] = 13
        elif string[i] == 'N':
            string[i] = 14
        elif string[i] == 'O':
            string[i] = 15
        elif string[i] == 'P':
            string[i] = 16
        elif string[i] == 'Q':
            string[i] = 17
        elif string[i] == 'R':
            string[i] = 18
        elif string[i] == 'S':
            string[i] = 19
        elif string[i] == 'T':
            string[i] = 20
        elif string[i] == 'U':
            string[i] = 21
        elif string[i] == 'V':
            string[i] = 22
        elif string[i] == 'W':
            string[i] = 23
        elif string[i] == 'X':
            string[i] = 24
        elif string[i] == 'Y':
            string[i] = 25
        elif string[i] == 'Z':
            string[i] = 26
    return string

def comeBack(string):
    for i in range(len(string)):
        if string[i] == 1:
            string[i] = 'A'
        elif string[i] == 2:
            string[i] = 'B'
        elif string[i] == 3:
            string[i] = 'C'
        elif string[i] == 4:
            string[i] = 'D'
        elif string[i] == 5:
            string[i] = 'E'
        elif string[i] == 6:
            string[i] = 'F'
        elif string[i] == 7:
            string[i] = 'G'
        elif string[i] == 8:
            string[i] = 'H'
        elif string[i] == 9:
            string[i] = 'I'
        elif string[i] == 10:
            string[i] = 'J'
        elif string[i] == 11:
            string[i] = 'K'
        elif string[i] == 12:
            string[i] = 'L'
        elif string[i] == 13:
            string[i] = 'M'
        elif string[i] == 14:
            string[i] = 'N'
        elif string[i] == 15:
            string[i] = 'O'
        elif string[i] == 16:
            string[i] = 'P'
        elif string[i] == 17:
            string[i] = 'Q'
        elif string[i] == 18:
            string[i] = 'R'
        elif string[i] == 19:
            string[i] = 'S'
        elif string[i] == 20:
            string[i] = 'T'
        elif string[i] == 21:
            string[i] = 'U'
        elif string[i] == 22:
            string[i] = 'V'
        elif string[i] == 23:
            string[i] = 'W'
        elif string[i] == 24:
            string[i] = 'X'
        elif string[i] == 25:
            string[i] = 'Y'
        elif string[i] == 26:
            string[i] = 'Z'
    return string


testNumber = input[0][0]

count = 0
start = 1

while count < testNumber:
    wordList = input[start].copy()
    wordList = translate(wordList)
    storage = []
    maxLength = 0
    for i in range(len(wordList)):
        string = wordList[i]
        outer = i
        X = []
        X.append(wordList[i])
        while outer != len(wordList)-1:
            if wordList[outer+1] - wordList[outer] <= 3:
                X.append(wordList[outer+1])
                outer += 1
            else:
                break
        if len(X)>=maxLength:
            maxLength = len(X)
            storage = X
    storage.reverse()

    print("".join(comeBack(storage)))

    count += 1
    start += 1