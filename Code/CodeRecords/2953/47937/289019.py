def gcd(x,y):
    if(y==1):
        return x-1
    if(x==0):
        return 100000000
    if(y==0):
        return 100000000
    if(x==y):
        return 100000000
    return gcd(y,x%y)+int(x/y)

n=int(input())

ans=n-1

i=2
while(i<n):
    ans=min(gcd(n,i),ans)
    i=i+1

print(ans,end="")
