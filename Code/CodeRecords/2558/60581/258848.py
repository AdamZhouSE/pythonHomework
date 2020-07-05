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
        if lst[i][j] == '{' or lst[i][j] == '}':
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

testNumber = input[0][0]

count = 0
start = 1

while count < testNumber:
    wordList = input[start].copy()
    if len(wordList) % 2 == 1:
        print(-1)
    else:
        half = int(len(wordList)/2)
        totalCount = 0
        for i in range(0,half):
            if wordList[i] == wordList[len(wordList)-1-i]:
                totalCount += 1
        print(totalCount)

    count += 1
    start += 1