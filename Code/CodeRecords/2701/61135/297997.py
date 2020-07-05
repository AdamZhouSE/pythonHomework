cell=[[0,0,0] for i in range(3)]
section=input()
section=section[1:len(section)-1]
section=section.split("],[")
section[0]=section[0][1:]
section[len(section)-1]=section[len(section)-1][:3]
player=0
winner=-1
WAYS_TO_WIN = ((0, 1, 2,), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7),(2, 5, 8),(0, 4, 8), (2, 4, 6))
for i in range(len(section)):
    if i%2==0:
        player=1
    else: player=2
    x=int(section[i][0])
    y=int(section[i][2])
    cell[x][y]=playey
    for row in range(3):
        if (cell[row][0] == cell[row][1] == cell[row][2] != 0) or(cell[0][row] == cell[1][row] == cell[2][row] != 0):
            winner = cell[row][row]
            break
    if (cell[0][0] == cell[1][1] == cell[2][2] != 0) or (cell[0][2] == cell[1][1] == cell[2][0] != 0):
        winner=cell[1][1]
    if(winner!=-1):
        if winner==1:
            print("A")
            break;
        else:
            print("B")
            break
flag=False
if winner==-1:
    for i in cell:
        flag= 0 in i
    if flag:
        print("Pending")
    else:print("Draw")