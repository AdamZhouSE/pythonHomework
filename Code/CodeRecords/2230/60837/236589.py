def reach(x,y,tx,ty):
    while (tx>0)&(ty>0):
        if (tx==x)&(ty==y):
            return True
        if tx>ty:
            tx-=ty
        else:
            ty-=tx
    return False

sx=int(input())
sy=int(input())
tx=int(input())
ty=int(input())
print(reach(sx,sy,tx,ty))
