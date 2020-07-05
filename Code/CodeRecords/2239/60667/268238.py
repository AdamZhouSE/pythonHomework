def validTicTacToe(board):
    l = [[6,1,8],[7,5,3],[2,9,4]]
    l_x, l_o = list(), list()
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                l_x.append(l[i][j])
            elif board[i][j] == "O":
                l_o.append(l[i][j])
    len_l_x = len(l_x)
    len_l_o = len(l_o)
    if len_l_x < len_l_o or len_l_x > len_l_o + 1:
        return False
        
    x_win = check_win(len_l_x,l_x)
        
    o_win = check_win(len_l_o, l_o)
    if x_win and o_win:
        return False
    if x_win and len_l_x == len_l_o:
        return False
    if o_win and len_l_x == len_l_o+1:
        return False
    return True
        
def check_win(n, l):
    if n >=3:
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1,n):
                    if l[j] + l[i] + l[k] == 15:
                            return True
    return False
b = input().split(',')
print(validTicTacToe(b))