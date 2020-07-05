ins=list(input())
dir=0
x,y=0,0
for i in range(len(ins)):
    ch=ins[i]
    if ch=="R":
        dir=(dir+1)%4
    elif ch=="L":
        if dir=='0':
            dir=3
        else:
            dir-=1
    else:
        if ch==0:
            y+=1
        elif ch==1:
            x+=1
        elif ch==2:
            y-=1
        else:
            x-=1
if dir!=0 or (x==0 and y==0):
    print(True)
else:
    print(False)