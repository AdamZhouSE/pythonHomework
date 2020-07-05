chess_list=[[0,0,0],[0,0,0],[0,0,0]]
process_list=eval(input())
length=len(process_list)
win=False
for i in range(length):
    if i%2==0:
        chess_list[process_list[i][0]][process_list[i][1]]="X"
    else:
        chess_list[process_list[i][0]][process_list[i][1]]="O"
for j in range(3):
        if chess_list[j][0]==chess_list[j][1] and chess_list[j][1]==chess_list[j][2]:
            if chess_list[j][0]=="X":
                print("A")
                win=True
                break
            elif chess_list[j][0]=="O":
                print("B")
                win=True
                break
        if chess_list[0][j]==chess_list[1][j] and chess_list[1][j]==chess_list[2][j]: 
            if chess_list[0][j]=="X":
                print("A")
                win=True
                break
            elif chess_list[0][j]=="O":
                print("B")
                win=True
                break
if chess_list[0][0]==chess_list[1][1] and chess_list[1][1]==chess_list[2][2]:
            if chess_list[0][0]=="X":
                print("A")
                win=True
            elif chess_list[0][0]=="O":
                print("B")
                win=Tru
if chess_list[2][0]==chess_list[1][1] and chess_list[1][1]==chess_list[0][2]:
            if chess_list[2][0]=="X":
                print("A")
                win=True
            elif chess_list[2][0]=="O":
                print("B")
                win=True
if not win:
    if length==9:
        print("Draw")
    else:
        print("Pending")