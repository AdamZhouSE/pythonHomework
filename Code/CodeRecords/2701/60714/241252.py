moves = [x[0: 3] for x in input()[1: -1].split("[")]
moves.pop(0)
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(0, len(moves)):
    if i % 2 is 0:
        board[int(moves[i][0])][int(moves[i][2])] = 1
    else:
        board[int(moves[i][0])][int(moves[i][2])] = 2
flag = False
for i in range(0, 3):
    if board[i] == [1, 1, 1]:
        print("A")
        flag = True
    elif board[i] == [2, 2, 2]:
        print("B")
        flag = True
if not flag:
    for i in range(0, 3):
        if board[0][i] == board[1][i] == board[2][i] == 1:
            print("A")
            flag = True
        elif board[0][i] == board[1][i] == board[2][i] == 2:
            print("B")
            flag = True
if not flag:
    if board[0][0] == board[1][1] == board[2][2] == 1:
        print("A")
        flag = True
    elif board[0][0] == board[1][1] == board[2][2] == 2:
        print("B")
        flag = True
if not flag:
    if board[0][2] == board[1][1] == board[2][0] == 1:
        print("A")
        flag = True
    elif board[0][2] == board[1][1] == board[2][0] == 2:
        print("B")
        flag = True
if not flag:
    full = True
    for i in range(0, 3):
        if 0 in board[i]:
            full = False
            break
    if full:
        print("Draw")
    else:
        print("Pending")
