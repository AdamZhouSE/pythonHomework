board = []
for i in range(5):
    board.append(list(map(int,input().split(' '))))
loc1 = []
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == 1:
            loc1 = [i,j]
            break
step = abs(loc1[0]-2) + abs(loc1[1]-2)
print(step)
