

def solve():
    li = input().split(",")
    board = [[] for i in range(3)]
    cntX = 0
    cntO = 0
    for i in range(len(li)):
        t = board[i]
        for j in list(li[i]):
            t.append(j)
            if j == "X": cntX += 1
            if j == "O": cntO += 1
    if cntO > cntX: return False
    if cntX - cntO > 1: return False

    cntWin = 0
    if board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] != " ": cntWin += 1
    if board[1][0] == board[1][1] and board[1][0] == board[1][2] and board[1][0] != " ": cntWin += 1
    if board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] != " ": cntWin += 1
    if board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] != " ": cntWin += 1
    if board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] != " ": cntWin += 1
    if board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] != " ": cntWin += 1
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != " ": cntWin += 1
    if board[2][0] == board[1][1] and board[2][0] == board[0][2] and board[2][0] != " ": cntWin += 1
    if cntWin > 1: return False
    return True

print(solve())

