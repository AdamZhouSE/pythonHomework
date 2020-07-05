n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split(','))))
if any(board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j] for i in range(n) for j in range(n)): 
    print(-1)
    quit()
row = sum(board[0])
col = sum(board[i][0] for i in range(n))
r = sum(board[0][i] != i % 2 for i in range(n))
c = sum(board[i][0] != i % 2 for i in range(n))
if n % 2 == 0:
    if not (row * 2 == n and col * 2 == n):
        print(-1)
        quit()
    print((min(r, n - r) + min(c, n - c))//2)
else:
    if not ((row == n // 2 or row == n // 2 + 1) and (col == n // 2 or col == n // 2 + 1)):
        print(-1)
    resr = n - r if row * 2 > n else r
    resc = n - c if col * 2 > n else c
    print((resr + resc)//2)
