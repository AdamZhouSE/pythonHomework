def func9():
    sx, sy, tx, ty = int(input()), int(input()), int(input()), int(input())
    flag = False
    while tx>0 and ty>0:
        if sx==tx and sy==ty:
            flag = True
        if tx>ty:
            tx -= max((tx-sx)//ty,1)*ty
        else:
            ty -= max((ty-sy)//tx,1)*tx
    print(flag)
    return
func9()