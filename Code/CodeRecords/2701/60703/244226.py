list = [[0 for i in range(0,3)] for i in range(0,3)];
def judge(list):
    if(
            (list[0][0]==1 and list[0][1]==1 and list[0][2]==1)
        or (list[1][0]==1 and list[1][1]==1 and list[1][2]==1)
        or (list[2][0]==1 and list[2][1]==1 and list[2][2]==1)
        or (list[0][0]==1 and list[1][0]==1 and list[2][0]==1)
        or (list[0][1]==1 and list[1][1]==1 and list[2][1]==1)
        or (list[0][2]==1 and list[1][2]==1 and list[2][2]==1)
        or (list[0][0]==1 and list[1][1]==1 and list[2][2]==1)
        or (list[2][0]==1 and list[0][2]==1 and list[1][1]==1)
    ):
        return 1;
    elif(
            (list[0][0] == 2 and list[0][1] == 2 and list[0][2] == 2)
            or (list[1][0] == 2 and list[1][1] == 2 and list[1][2] == 2)
            or (list[2][0] == 2 and list[2][1] == 2 and list[2][2] == 2)
            or (list[0][0] == 2 and list[1][0] == 2 and list[2][0] == 2)
            or (list[0][1] == 2 and list[1][1] == 2 and list[2][1] == 2)
            or (list[0][2] == 2 and list[1][2] == 2 and list[2][2] == 2)
            or (list[0][0] == 2 and list[1][1] ==2 and list[2][2] == 2)
            or (list[2][0] == 2 and list[0][2] == 2 and list[1][1] == 2)
    ):
        return 2;
    else:
        return 0;
moves  =eval(input());
res=0;
for i in range(0,len(moves)):
    x=moves[i][0];
    y=moves[i][1];
    if(i%2==0):
        list[x][y] = 1;
    else:
        list[x][y]=2;
    res = judge(list);
    if(res==1 or res==2):
        break;
if(res==0):
    if(len(moves)==9):
        print("Draw");
    else:
        print("Pending");
else:
    if(res==1):
        print("A");
    else:
        print("B");