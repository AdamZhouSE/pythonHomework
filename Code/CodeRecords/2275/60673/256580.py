#

n = int(input())
board = []
canChange = 0
rowDiff = 0
colDiff = 0
for i in range(n):
    board.append(str(input()).split(","))
    for j in range(n):
        board[i][j] = int(board[i][j])

# 判断是否能变换成棋盘
if (board[0][0] ^ board[0][n - 1] ^ board[n - 1][0] ^ board[n - 1][n - 1] == 0):
    for i in range(n):
        numOfOne1 = 0  # 行1的个数
        numOfOne2 = 0  # 列1的个数
        for j in range(n):
            numOfOne1 += board[i][j]
            numOfOne2 += board[j][i]
        if (numOfOne1 < int(n / 2) | numOfOne1 > int((n + 1) / 2) | numOfOne2 < int(n / 2) | numOfOne2 > int((n + 1) / 2)):
            canChange = -1
            break
else:
    canChange = -1

for i in range(n):
    rowDiff += (board[i][0] == i % 2)
    colDiff += (board[0][i] == i % 2)

if (canChange != -1):
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
