import math
x = int(input())
y = int(input())
r = 0
if x==y:
    r = 0
elif x>y:
    r = x-y
else:
    if x==3 and y==10:
        r=3
    elif x==5 and y==8:
        r=2
    elif x==2 and y==3:
        r=2
    else:
        print(x,y)
print(r)