sx=int(input())
sy=int(input())
tx=int(input())
ty=int(input())
mark=0
while(tx>=1 and ty>=1):
    if(tx==sx and ty==sy):
        mark=1
        break
    elif(tx==ty):
        break
    if(tx>ty):
        tx=tx-ty
    elif(tx<ty):
        ty=ty-tx

if(mark==1):
    cons=True
else:
    cons=False
print(cons)
