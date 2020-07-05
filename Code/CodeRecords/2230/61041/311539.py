sx=eval(input())
sy=eval(input())
tx=eval(input())
ty=eval(input())
isAble=False
while (tx>=sx)&(ty>=sy):
    if (tx==sx)&(ty==sy):
        isAble=True
        break
    elif tx>ty:
        tx-=ty
    elif tx<ty:
        ty-=tx
print(isAble)