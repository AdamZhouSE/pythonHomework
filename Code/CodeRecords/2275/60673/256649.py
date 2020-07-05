#

n = int(input())
board = []
canChange = 0
rowDiff = 0
colDiff = 0
rowSum = 0
colSum = 0
for i in range(n):
    board.append(str(input()).split(","))
    for j in range(n):
        board[i][j] = int(board[i][j])

# 判断是否能变换成棋盘
for i in range(n):
    for j in range(n):
        if (board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]==1):
            canChange = -1

for i in range(n):
    rowSum += board[0][i]
    colSum += board[i][0]
    rowDiff += (board[i][0] == i % 2)
    colDiff += (board[0][i] == i % 2)

if (n / 2 > rowSum | rowSum > (n + 1) / 2):
    canChange = -1

if (n / 2 > colSum | colSum > (n + 1) / 2):
    canChange = -1

if (canChange >= 0):
    # 如果是奇数
    if (n % 2):
        if (rowDiff % 2):
            rowDiff = n - rowDiff
        if (colDiff % 2):
            colDiff = n - colDiff
    else:
        rowDiff = min(n - rowDiff, rowDiff)
        colDiff = min(n - colDiff, colDiff)
    canChange = (rowDiff + colDiff) / 2

print(canChange)
