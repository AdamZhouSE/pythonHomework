def judge(board):
    i = 0
    judgeX = 0
    judgeY = 0
    judgeL = 0
    judgeR = 0
    while i < 3:
        j = 0
        while j < 3:
            judgeX += board[i][j]
            judgeY += board[j][i]
            if (i == j):
                judgeL += board[i][j]
            if(((i==0)and(j==2))or((i==2)and(j==0))or((i==1)and(j==1))):
                judgeR += board[i][j]
            j += 1
        if((judgeX == 30)or(judgeY == 30)):
            return "A"
        elif((judgeX == 33)or(judgeY == 33)):
            return "B"
        else:
            judgeX = 0
            judgeY = 0
        i += 1
    if((judgeL == 30)or(judgeR == 30)):
        return "A"
    elif((judgeL == 33)or(judgeR==33)):
        return "B"
    else:
        return "D"


#main-----
source = input()
source = source[1:len(source)-1]

#格式转化-----
moveList = []
i = 1
while i < len(source):
    str1 = ""
    str2 = ""
    while source[i] != ',':
        str1 += source[i]
        i += 1
    i += 1
    while source[i] != ']':
        str2 += source[i]
        i += 1
    i += 3
    moveList.append([int(str1),int(str2)])
#进行比赛-----
chessBoard = [[0,0,0],
              [0,0,0],
              [0,0,0]]
i = 0
while i <=len(moveList):
    if i == len(moveList):
        if(i == 9):
            print("Draw")
        else:
            print("Pending")
    else:
        chessBoard[moveList[i][0]][moveList[i][1]] = i%2+10
        result = judge(chessBoard)
        if(result == "A"):
            print("A")
            i = len(moveList) + 10
        elif(result == "B"):
            print("B")
            i = len(moveList) + 10
    i += 1
            
    