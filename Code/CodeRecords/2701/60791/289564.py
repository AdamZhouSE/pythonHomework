move = eval(input())
board = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(move)):
    x,y = move[i][0],move[i][1]
    board[x][y] = 1 if i%2 ==0 else 2

if(len(move) < 5):
    print('Pending')
else:
    res = 'n'
    for i in range(3):
        if(board[i] == [1,1,1]):
            res = 'A'
            break
        elif(board[i] == [2,2,2]):
            res = 'B'
            break
        elif(board[0][i] == 1 and board[1][i] == 1 and board[2][i] == 1):
            res = 'A'
            break
        elif(board[0][i] == 2 and board[1][i] == 2 and board[2][i] == 2):
            res = 'B'
            break
    if((board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1)or(board[2][0] == 1 and board[1][1] == 1 and board[0][2] == 1)):
        res = 'A'
        print('A')
    elif((board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2)or(board[2][0] == 2 and board[1][1] == 2 and board[0][2] == 2)):
        res = 'B'
        print('B')
    elif(res != 'A' and res != 'B'):
        if(len(move) ==  9):
            print('Draw')
        else:
            count = [0,0,0]
            re = False
            for i in range(3):
                for x in range(3):
                    count[board[i][x]] += 1
                if(count[1] == 2 and count[0] == 1):
                    print('Pending')
                    re = True
                    break
                if(count[2] == 2 and count[0] == 1 and len(move)!=8):
                    print('Pending')
                    re = True
                    break
                elif(count[2] == 2 and count[0] == 1 and len(move)==8):
                    print('Draw')
                    re = True
                    break
                if(count[1] == 1 and count[0] == 2 and len(move)<7):
                    print('Pending')
                    re = True
                    break
                if(count[2] == 1 and count[0] == 2 and len(move)<6):
                    print('Pending')
                    re = True
                    break
                if(count[0] == 3 and len(move) < 5):
                    print('pending')
                    re = True
                    break

                count = [0,0,0]
                for x in range(3):
                    count[board[x][i]] += 1
                if(count[1] == 2 and count[0] == 1):
                    print('Pending')
                    re = True
                    break
                if(count[2] == 2 and count[0] == 1 and len(move)!=8):
                    print('Pending')
                    re = True
                    break
                elif(count[2] == 2 and count[0] == 1 and len(move)==8):
                    print('Draw')
                    re = True
                    break
                if(count[1] == 1 and count[0] == 2 and len(move)<7):
                    print('Pending')
                    re = True
                    break
                if(count[2] == 1 and count[0] == 2 and len(move)<7):
                    print('Pending')
                    re = True
                    break
                if(count[0] == 3 and len(move) < 5):
                    print('pending')
                    re = True
                    break
                count = [0,0,0]
            
            for i in range(3):
                count[board[i][i]] += 1
            if(count[1] == 2 and count[0] == 1):
                print('Pending')
                re = True
            if(count[2] == 2 and count[0] == 1 and len(move)!=8):
                print('Pending')
                re = True
            elif(count[2] == 2 and count[0] == 1 and len(move)==8):
                print('Draw')
                re = True
            if(count[1] == 1 and count[0] == 2 and len(move)<7):
                print('Pending')
                re = True
            if(count[2] == 1 and count[0] == 2 and len(move)<7):
                print('Pending')
                re = True
            if(count[0] == 3 and len(move) < 5):
                print('pending')
                re = True
            count = [0,0,0]
            for i in range(3):
                count[board[2-i][i]] += 1
            if(count[1] == 2 and count[0] == 1):
                print('Pending')
                re = True
            if(count[2] == 2 and count[0] == 1 and len(move)!=8):
                print('Pending')
                re = True
            elif(count[2] == 2 and count[0] == 1 and len(move)==8):
                print('Draw')
                re = True
            if(count[1] == 1 and count[0] == 2 and len(move)<7):
                print('Pending')
                re = True
            if(count[2] == 1 and count[0] == 2 and len(move)<7):
                print('Pending')
                re = True
            if(count[0] == 3 and len(move) < 5):
                print('pending')
                re = True
            count = [0,0,0]
            if(re == False):
                print('Draw')
    else:
        print(res)	

             
             
            