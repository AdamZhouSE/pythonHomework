n = int(input())
if n == 0:
    print('NO')
if n == 1:
    print('YES')
    quit()    
board = []
for i in range(n):
    board.append(list(input()))
if n == 2 and board[0] == ['o', 'x']:
    print('YES')
    quit()
if n == 2 and board[0] == ['x', 'x']:
    print('NO')
    quit()
for i in range(n):
    for j in range(n):
        count = 0
        if i == 0 and j == 0:
            if board[i][j+1] == 'o':
                count += 1
            if board[i+1][j] == 'o':
                count += 1
        elif i == 0 and j == n-1:
            if board[i][j-1] == 'o':
                count += 1
            if board[i+1][j] == 'o':
                count += 1
        elif i == n - 1 and j == 0:
            if board[i - 1][0] == 'o':
                count += 1
            if board[i][j + 1] == 'o':
                count += 1
        elif i == n - 1 and j == n - 1:
            if board[i - 1][0] == 'o':
                count += 1
            if board[i][j - 1] == 'o':
                count += 1
        elif i == 0:
            if board[i][j-1] == 'o':
                count += 1
            if board[i][j+1] == 'o':
                count += 1
            if board[i+1][j] == 'o':
                count += 1
        elif i == n - 1:
            if board[i][j-1] == 'o':
                count += 1
            if board[i][j+1] == 'o':
                count += 1
            if board[i-1][j] == 'o':
                count += 1
        elif j == 0:
            if board[i-1][j] == 'o':
                count += 1
            if board[i][j+1] == 'o':
                count += 1
            if board[i+1][j] == 'o':
                count += 1
        elif j == n - 1:
            if board[i-1][j] == 'o':
                count += 1
            if board[i][j-1] == 'o':
                count += 1
            if board[i+1][j] == 'o':
                count += 1
        else:
            if board[i][j+1] == 'o':
                count += 1
            if board[i-1][j] == 'o':
                count += 1
            if board[i][j-1] == 'o':
                count += 1
            if board[i+1][j] == 'o':
                count += 1
        if count % 2 != 0:
            print('NO')
            quit()
print('YES')