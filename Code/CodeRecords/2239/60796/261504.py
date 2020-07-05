def win():
    r = []
    # 行
    for i in range(len(board)):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            r.append(board[i][0])
    # 列
    for i in range(len(board)):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            r.append(board[2][i])
    # 对角线
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        r.append(board[0][0])
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        r.append(board[2][0])
    return r


board = []
for i in range(3):
    board.append([None, None, None])

s = input().split(",")
nX = 0
nO = 0
for i in range(len(s)):
    if s[i] != "   ":
        for j in range(3):
            board[i][j] = s[i][j]
            if s[i][j] == "X":
                nX = nX + 1
            if s[i][j] == "O":
                nO = nO + 1
result = True
# 不可能的情况：
# 1：不是轮流放置
if nO > nX or nX - 1 > nO:
    result = False
# 2:有两个胜者
r = win()
if r.__contains__("X") and r.__contains__("O"):
    result = False
# 3:某个选手赢了两次:
if r.count("X")>1 or r.count("O")>1:
    result=False
print(result)




