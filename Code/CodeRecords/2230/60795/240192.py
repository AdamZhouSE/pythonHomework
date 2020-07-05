sx=int(input())
sy=int(input())
ex=int(input())
ey=int(input())
aa=0
while sx<=ex|sy<=ey:
    sy=sy+sx
    if sx==ex:
        if sy==ey:
            print('True')
            aa=1
            break
    sx=sx+sy
    if sx==ex:
        if sy==ey:
            print('True')
            aa=1
            break
if aa==0:
    print('False')