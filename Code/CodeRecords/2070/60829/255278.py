def exp(x):
    for i in range(0,len(x)):
        if x[i]=='.':
            break
    if 6+i-len(x)>0:
        x=x+'0'*(6+i-len(x))
    else:
        x=x[0:i+6]
    return x
a=float(input())
b=int(input())
if b>0:
    x=1
    for i in range(0,b):
        x=x*a
    print(exp(str(x)))
elif b==0:
    print(1)
else:
    b=-1*b
    x=1
    for i in range(0,b):
        x=x/a
    print(exp(str(x)))
    