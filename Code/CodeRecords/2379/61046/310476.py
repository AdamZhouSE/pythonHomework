inst=input()
x = 0
y = 0
d = 0
inst=inst*4
inst=list(inst)
for i in inst:
    if i == 'G':
        if d==0:
            y+=1
        elif d==2:
            y-=1
        elif d==1:
            x+=1
        else:
            x-=1
    elif i == 'L':
        if d==0:
            d=3
        else:
            d-=1
    elif i == 'R':
        if d == 0:
            d= 3
        else:
            d += 1
if x == 0 and y == 0:
    print("True")
else:
    print("False")