def j(b):
    while b>0:
        if b%5==0:
            b=b//5
        elif b%2==0:
            b=b//2
        elif b==1:
            return True
        else:
            return False
a=int(input())
b=int(input())
if a%b==0:
    print(int(a/b))
elif  not j(b):
    print("0.(6)")
else:
    print(float(a/b))