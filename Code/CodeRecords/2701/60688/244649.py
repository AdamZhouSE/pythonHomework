cell=[[0,0,0] for i in range(3)];
steps=input();
steps=steps[1:len(steps)-1];
steps.split(",");
player=0;
winner=-1;
WAYS_TO_WIN = ((0, 1, 2,), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
for i in range(len(steps)):
    #[0,0],[2,0],[1,1],[2,1],[2,2](str)
    #首先是赢的条件，然后判断是否为满（是平局），否 pending，
    if i%2==0:
        player=1;
    else: player=2;
    x=int(steps[i][1]);
    y=int(steps[i][3]);
    cell[x][y]=player;
    for row in WAYS_TO_WIN:
        if cell[row[0]] == cell[row[1]] == cell[row[2]] != 0:
            winner = cell[row[0]];
            break;
    if(winner!=-1):
        if winner==1:
            print("A");
            break;
        else:
            print("B");
            break;
flag=False;
if winner==-1:
    for i in cell:
        flag= 0 in i;
    if flag:
        print("Pending");
    else:print("Draw");
