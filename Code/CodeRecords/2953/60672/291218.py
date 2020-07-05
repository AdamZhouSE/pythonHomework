def gcd(x,y):
    x=int(x)
    y=int(y)
    if y==1:
        return x-1
    elif x==0:
        return 10000000
    elif y==0:
        return 10000000
    elif x==y:
        return 10000000
    else:
        return gcd(y,x%y)+int(x/y)

n=int(input())
m=n-1
for i in range(2,n):
    m=min(gcd(n,i),m)
print(m,end='')
    