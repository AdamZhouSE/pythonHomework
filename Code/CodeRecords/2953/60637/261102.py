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
else:
    for i in range(0,n):
        record=min(gcd(n,i),record)
    print(record,end="")

