def check(board):
    win = 0
    if board[0][0]==board[0][1] and board[0][0]==board[0][2]:
        win+=1
    if board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        win+=1
    if board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        win+=1
    if board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        win+=1
    if board[0][1] == board[1][1] and board[0][1] == board[2][1]:
        win+=1
    if board[0][2] == board[1][2] and board[0][2] == board[2][2]:
        win+=1
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        win+=1
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        win+=1
    return win
        

if __name__ == "__main__":
    board = input().split(',')
    player1,player2 = 0,0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]=='X':
                player1+=1
            elif board[i][j]=='O':
                player2+=1
    if player1-player2>1 or player2>player1:
        print("False")
    else:
        if(check(board)>=2):
            print("False")
        else:
            print("True")