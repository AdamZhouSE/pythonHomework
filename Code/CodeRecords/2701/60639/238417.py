def check(board,moves):
    for i in range(3):
            if board[i][0]==board[i][1] and board[i][1]==board[i][2]:
                if board[i][0] == 'X':
                    return 'A'
                elif board[i][0] == 'O':
                    return 'B'
                else:
                    return 'Pending'
            elif board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                if board[0][i] == 'X':
                    return 'A'
                elif board[0][i] == 'O':
                    return 'B'
                else:
                    return 'Pending'
            elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
                if board[0][0] == 'X':
                    return 'A'
                elif board[0][0] == 'O':
                    return 'B'
                else:
                    return 'Pending'
            elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
                if board[0][2] == 'X':
                    return 'A'
                elif board[0][2] == 'O':
                    return 'B'
                else:
                    return 'Pending'
    if len(moves)==9:
        return 'Draw'
    else:
        return 'Pending'

def setBoard(moves):
    board=[[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    for i in range(len(moves)):
        row=moves[i][0]
        column=moves[i][1]
        if i%2==0:
            board[row][column] = 'X'
        else:
            board[row][column] = 'O'
    return(board)

def transStep(Str):
    Str=Str[2:len(Str)-2].split('],[')
    moves=[]
    for i in range(len(Str)):
        step=Str[i].split(',')
        moves.append(step)
    for i in range(len(moves)):
        for j in range(2):
            moves[i][j]=int(moves[i][j])
    return moves

def main():
    inp=input()
    moves=transStep(inp)
    board=setBoard(moves)
    result=check(board,moves)
    print(result)

main()