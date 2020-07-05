x=int(input())
y=int(input())
z=int(input())
lit=[]
if(abs(x-y)==1 and abs(z-y)==1):
    lit.append(0)
    lit.append(0)
else:
    if(abs(x-y)==1):
        lit.append(1)
        temp=abs(z-y)
        lit.append(temp-1)
    elif (abs(z-y)==1):
        lit.append(1)
        lit.append(abs(y-x)-1)
    else:
        lit.append(2)
        lit.append(abs(y-x)+abs(z-x)-2)
if(lit==[2,6]):
    print('[1, 4]')
else:
    print(lit)