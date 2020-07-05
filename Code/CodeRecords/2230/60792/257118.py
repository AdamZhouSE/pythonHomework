def reachingEnd(sx,sy,tx,ty):
    while tx>sx and ty>sy:
        if tx>ty:
            tx=tx%ty
        else:
            ty=ty%tx
    if tx==sx and (ty-sy)%sx==0:
        return True
    if ty==sy and (tx-sx)%sy==0:
        return True
    return False

sx=int(input())
sy=int(input())
tx=int(input())
ty=int(input())
print(reachingEnd(sx,sy,tx,ty))