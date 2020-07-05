def win(player):
    for i in range(3):
        if all(board[i][j]==player for j in range(3)): #判断行
            return True
        if all(board[j][i]==player for j in range(3)): #判断列
            return True
    if player==board[0][0]==board[1][1]==board[2][2]:
        return True
    if player==board[0][2]==board[1][1]==board[2][0]:
        return True
    return False
board=input().split(",")
x_count=sum(row.count('X') for row in board)
o_count=sum(row.count('O') for row in board)
if (win('X') and x_count-o_count!=1) or (win('O') and x_count!=o_count) or o_count not in {x_count-1,x_count}:
    print(False)
else:
    print(True)

