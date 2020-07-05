sx=int(input())
sy=int(input())
tx=int(input())
ty=int(input())
flag=False
while sx<=tx and sy<=ty:
    if sx==tx and sy==ty:
        flag=True
    if tx>=ty:
        tx=tx-max(ty*((tx-sx)/ty),ty)
    else:
        ty=ty-max(tx*((ty-sy)/tx),tx)
if flag==True:
    print(flag)
else:
    print(False)