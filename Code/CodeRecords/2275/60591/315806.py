def cal(test):
    now = 1
    result1 = 0
    for m in test:
        result1 += now ^ m
        now = 1- now
    now = 0
    result2 = 0
    for m in test:
        result2 += now ^ m
        now = 1 - now
    return min(result1,result2)

def check(board):
    lines = [board[0]]
    result = []
    for t in board:
        if (t == lines[0]):
            result.append(1)
        else:
            if (len(lines) == 1):
                lines.append(t)
            else:
                if (lines[1] != t):
                    return -1
            result.append(0)
    return cal(result)



n = eval(input())
board = []
while(n > 0 ):
    n -= 1
    temp = list(map(eval,input().split(",")))
    board.append(temp)
reverseBoard = []
for i in range(len(board)):
    temp = []
    for j in range(len(board)):
        temp.append(board[j][i])
    reverseBoard.append(temp)
a = check(board)
b = check(reverseBoard)
if(a == -1 or b == -1):
    print(-1)
else:
    result = a + b
    if(result % 2 == 1):
        print(-1)
    else:
        print(int(result/2))