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
    m = input[start][0]
    n = input[start][1]
    wordList = input[start+1].copy()
    picture = [[0 for i in range(n)]for i in range(m)]
    for i in range(m):
        for j in range(n):
            picture[i][j] = wordList[n*i+j]
    outPutNumber = 0
    startX = 0
    startY = 0
    while outPutNumber < m*n:
        if startX==0 and startY!=n-1:
            print(picture[startX][startY],end=" ")
            picture[startX][startY] = 0
            outPutNumber += 1
            startY += 1
        elif startY==n-1 and startX!=m-1:
            print(picture[startX][startY],end=" ")
            picture[startX][startY] = 0
            outPutNumber += 1
            startX += 1
        elif startX==m-1 and startY!=0:
            print(picture[startX][startY],end=" ")
            picture[startX][startY] = 0
            outPutNumber += 1
            startY -= 1
        elif startY==0 and picture[startX-1][startY]!=0:
            print(picture[startX][startY],end=" ")
            picture[startX][startY] = 0
            outPutNumber += 1
            startX -= 1
        elif picture[startX-1][startY]==0 and picture[startX][startY+1]!=0:
            print(picture[startX][startY],end=" ")
            picture[startX][startY] = 0
            outPutNumber += 1
            startY += 1
        elif picture[startX][startY+1]==0 and picture[startX+1][startY]!=0:
            print(picture[startX][startY], end=" ")
            picture[startX][startY] = 0
            outPutNumber += 1
            startX += 1
        elif picture[startX+1][startY]==0 and picture[startX][startY-1]!=0:
            print(picture[startX][startY], end=" ")
            picture[startX][startY] = 0
            outPutNumber += 1
            startY -= 1
        elif picture[startX][startY-1]==0 and picture[startX-1][startY]!=0:
            print(picture[startX][startY],end=" ")
            picture[startX][startY] = 0
            outPutNumber += 1
            startX -= 1
        elif picture[startX][startY+1]==0 and picture[startX][startY-1]==0 and picture[startX+1][startY] and picture[startX-1][startY]==0:
            print(picture[startX][startY],end=" ")
            print()
            picture[startX][startY] = 0
            outPutNumber += 1
        else:
            print(picture[startX][startY], end=" ")
            print()
            break

    count += 1
    start += 2
