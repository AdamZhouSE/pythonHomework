def checkwin():
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2] and not board[i][0]==' ':
           return True
        if board[0][i]==board[1][i] and board[1][0]==board[2][i] and not board[0][i]==' ':
            return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and not board[0][0]==' ':
        return True
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and not board[0][0]==' ':
        return True
    return False


board = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

string = input()[1:-1]
li = []
for i in string:
    if i.isdigit():
       li.append(int(i))
player = "A"
for i in range(0,len(li),2):
    board[li[i]][li[i+1]]="X" if player == "A" else "O"    
    if checkwin():
        print(player)
        exit()
    player = "B" if player == "A" else "A"
print("Pending")