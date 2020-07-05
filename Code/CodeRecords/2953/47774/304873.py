n=int(input())
ans=n-1

def gcd(x,y):
    if y==1:
        return x-1
    if x==0:
        return 10000
    if y==0:
        return 10000
    if x==y:
        return 10000
    return gcd(y,x%y)+int(x/y)  

for i in range(2,n):
    ans=min(gcd(n,i),ans)
print(ans,end="")