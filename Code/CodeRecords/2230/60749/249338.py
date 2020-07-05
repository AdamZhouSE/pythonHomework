sx=int(input())
sy=int(input())
tx=int(input())
ty=int(input())
def judge(sx,sy,tx,ty):
    while tx>sx and ty>sy:
        if tx>ty:
            tx=tx%ty
        else:
            ty=ty%tx
    if tx==sx:
        return (ty-sy)%tx==0
    if ty==sy:
        return (tx-sx)%ty==0
    return False
print(judge(sx,sy,tx,ty))