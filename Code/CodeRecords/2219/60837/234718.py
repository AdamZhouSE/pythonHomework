import math

a=int(input())
b=math.sqrt(a)
c=0
y=0
while c<=b:
    d=c
    while d<=b:
        if c**2+d**2==a:
            y=1
            break
        d+=1
    if y==1:
        break
    c+=1
if y==1:
    print("True")
else:
    print("False")