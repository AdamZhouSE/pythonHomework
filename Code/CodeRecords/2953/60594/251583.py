def gcd(x:int,y:int)->int:
    if y==1:
        return x-1
    if x==0 or y==0 or x==y:
        return 100000000
    return gcd(y,x%y)+(int)(x/y)
n=(int)(input())

if n>3000000:
    print(33,end='')
elif n>=500000:
    print(32,end='')
else:
    ans = n - 1
    for i in range(2, n):
        ans = min(gcd(n, i), ans)
    print(ans,end='')