n=int(input())
def gcd(n,i):
    if(i==n-1):
        return n-1
    if(n%i==0):
        return int(n/i)-1
    else:
        count=int(n/i)
        next=n%i
        return gcd(i,next)+count
if(n!=1):
    out=10000000000000
    for i in range(1,n):
        out=min(out,gcd(n,i))
        print(out,end="")
else:
    print(0,end="")