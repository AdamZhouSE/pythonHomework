def solve(board:list):
    n = len(board)
    rowSum = 0
    colSum = 0
    rowDiff = 0
    colDiff = 0
    for i in range(n):
        for j in range(n):
            if board[0][0]^board[i][0]^board[0][j]^board[i][j]!=0:
                return -1
    for i in range(n):
        rowSum += board[0][i]
        colSum += board[i][0]
        if board[i][0] == i % 2:
            rowDiff += 1
        if board[0][i] == i % 2:
            colDiff += 1
    if n//2 > rowSum or rowSum>(n+1)//2:
        return -1
    if n//2 > colSum or colSum>(n+1)//2:
        return -1
    if n % 2 != 0:
        if rowDiff %2!=0:
            rowDiff = n - rowDiff
        if colDiff%2!=0:
            colDiff = n - colDiff
    else:
        rowDiff = min(n-rowDiff,rowDiff)
        colDiff = min(n-colDiff,colDiff)
    return (rowDiff+colDiff)//2


n = eval(input())
board = []
for i in range(n):
    row = list(map(int,input().split(',')))
    board.append(row)
print(solve(board))




