# tag

board=input().split(",")
xNum = sum([sum([x == 'X' for x in line]) for line in board])
oNum = sum([sum([x == 'O' for x in line]) for line in board])

if (xNum != oNum) and (xNum - oNum != 1):
    print("False")
else:
    
    # 这一段来自checkIO上x-o-referee最简洁的解法
    cols = map(''.join, zip(*board))
    diag = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(board)]))
    lines = board + list(cols) + list(diag)

    oWin = True if 'OOO' in lines else False
    xWin = True if 'XXX' in lines else False

    if oWin and xWin:
        print("False")
    elif oWin and (xNum != oNum):
        print("False")
    elif xWin and (xNum - oNum != 1):
        print("False")
    else:
        print("True")