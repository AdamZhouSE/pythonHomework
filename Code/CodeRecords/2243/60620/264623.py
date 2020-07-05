p=int(input())
q=int(input())
def gcd(x,y):
    while(y!=0):
        x,y=y,x%y
    return x
k=p*q//gcd(p,q)
if((k//p)%2==0):
    print(0)
else:
    if((k//q)%2==0):
        print(2)
    else:
        print(1)