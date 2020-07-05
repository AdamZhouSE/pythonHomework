def dt(board):
    xNum = sum([sum([x == 'X' for x in line]) for line in board])
    oNum = sum([sum([x == 'O' for x in line]) for line in board])
    if (xNum != oNum) and (xNum - oNum != 1):
        return False
    cols = map(''.join, zip(*board))
    diag = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(board)]))
    lines = board + list(cols) + list(diag)
    oWin = True if 'OOO' in lines else False
    xWin = True if 'XXX' in lines else False
    if oWin and xWin:
        return False
    if oWin and (xNum != oNum):
        return False
    if xWin and (xNum - oNum != 1):
        return False
    return True
if __name__ == '__main__':
    print(dt([i for i in input().split(',')]))
