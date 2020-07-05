sx=int(input())
sy=int(input())
tx=int(input())
ty=int(input())

def cal(sx,sy,tx,ty):
    if(sx>tx or sy>ty):return False
    if(sx==tx and sy==ty):return True
    a=False
    k=sx+sy
    a=a or cal(k,sy,tx,ty)
    a=a or cal(sx, k, tx, ty)
    return a

print(cal(sx,sy,tx,ty))
