string=input().split(",");
board=[];
for i in range(3):
    board.append(list(string[i]));
count=0;
X_count=0;
O_count=0;
for i in range(3):
    if(board[0][i]==board[1][i]==board[2][i]):
        count+=1;
    if(board[i][0]==board[i][1]==board[i][2]):
        count+=1;
    X_count+=board[i].count("X");
    O_count+=board[i].count("O");
if(board[0][0]==board[1][1]==board[2][2]):
    count+=1;
if(board[0][2]==board[1][1]==board[2][0]):
    count+=1;
if(count>1)|(X_count<O_count)|(X_count-O_count>=2):
    print("False");
else:
    print("True");