moves=input();
Board=[[0,0,0],[0,0,0],[0,0,0]];
count=0;
for j in range(len(moves)):
    if(j%2==0):
        Board[moves[j][0]][moves[j][1]]="X";
    else:
        Board[moves[j][0]][moves[j][1]] = "O";
    for i in range(3):
        if(Board[i][0]==Board[i][1]==Board[i][2]=="X"):
            print("A");
            count=1;
        elif(Board[i][0]==Board[i][1]==Board[i][2]=="O"):
            print("B");
            count = 1;
        elif(Board[0][i]==Board[1][i]==Board[2][i]=="X"):
            print("A");
            count = 1;
        elif (Board[0][i] == Board[1][i] == Board[2][i] == ""):
            print("B");
            count = 1;
        if(count==1):
            break;
    if(Board[0][0]==Board[1][1]==Board[2][2]=="X"):
        print("A");
        count = 1;
    elif(Board[0][0]==Board[1][1]==Board[2][2]=="O"):
        print("B");
        count = 1;
    elif (Board[0][2] == Board[1][1] == Board[2][0] == "X"):
        print("A");
        count = 1;
    elif (Board[0][2] == Board[1][1] == Board[2][0] == "O"):
        print("B");
        count = 1;
    if(count==1):
        break;
for i in Board:
    if count==0:
        if(0 in i):
            print("Pending")
            count=1;
            break;
if(count==0):
    print("Draw")