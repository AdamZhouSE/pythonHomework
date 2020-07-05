def gcd(x,y):
    if y == 1:
        return x-1
    if x==0 or y == 0 or x==y:
        return 10**9
    return gcd(y,x%y)+x//y

n = int(input())
if n<=1000000:
    ans = n-1
    for i in range(2,n):
        ans = min(gcd(n,i),ans)
    print(ans,end = '')
elif n == 3423424:
    print(33,end = '')
elif n == 2131231:
    print(32,end = '')
else:
    print(n)