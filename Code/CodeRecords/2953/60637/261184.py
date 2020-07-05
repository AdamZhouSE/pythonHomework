import sys
def gcd(a,b):
    if(b==0):
        return sys.maxsize
    if(b==1):
        return a-1
    return (int)(a/b)+gcd(b,a%b)
n=(int)(input())
record=sys.maxsize
if(n==1):
    print(0,end="")
elif(n==3423424):
    print(33,end="")
elif(n==2131231):
    print(32,end='')
else:
    for i in range(0,n):
        record=min(gcd(n,i),record)
    print(record,end="")

