n = eval(input())
board = []
for i in range(n):
    board.append(list(input()))
isOK = True
for i in range(n):
    for j in range(n):
        count = 0
        if j-1>=0:
            if board[i][j-1] == 'o':
                count = count + 1
        if j+1<n:
            if board[i][j+1] == 'o':
                count = count + 1
        if i-1>=0:
            if board[i-1][j] == 'o':
                count = count +1
        if i+1<n:
            if board[i+1][j] == 'o':
                count = count + 1
        if count % 2 != 0:
            isOK = False
            break
if isOK:
    print('YES')
else:print('NO')