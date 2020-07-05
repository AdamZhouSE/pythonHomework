methods = input()
a = []
b = ''
i = 0
while i < len(methods):
    if methods[i]>='0' and methods[i]<='9' :
        b += methods[i]
        j = i+1
        while methods[j]>='0' and methods[j]<='9':
            b += methods[j]
            j += 1
            i += 1
        a.append(b)
        b = ''
    i += 1

board = [[0 for i in range(3)] for i in range(3)]
count = 0
signal = 'X'
judge = False
while count < len(a):
    if count % 4 == 0:
        signal = 'X'
    else:
        signal = 'O'
    if a[count]=='0' and a[count+1]=='0':
        board[0][0] = signal
    if a[count]=='0' and a[count+1]=='1':
        board[0][1] = signal
    if a[count]=='0' and a[count+1]=='2':
        board[0][2] = signal
    if a[count]=='1' and a[count+1]=='0':
        board[1][0] = signal
    if a[count]=='1' and a[count+1]=='1':
        board[1][1] = signal
    if a[count]=='1' and a[count+1]=='2':
        board[1][2] = signal
    if a[count]=='2' and a[count+1]=='0':
        board[2][0] = signal
    if a[count]=='2' and a[count+1]=='1':
        board[2][1] = signal
    if a[count]=='2' and a[count+1]=='2':
        board[2][2] = signal
    for i in range(0,3):
        if (board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][2] != 0)\
                or(board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[2][i] != 0)\
                or(board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1] != 0)\
                or(board[2][0]==board[1][1] and board[1][1]==board[0][2] and board[1][1] != 0):
            if signal=='X':
                print("A")
            else:
                print("B")
            judge = True
            break
    count += 2
if not judge:
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == 0:
                judge = True
    if judge:
        print("Pending")
    else:
        print("Draw")