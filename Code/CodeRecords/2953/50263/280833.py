def gcd(x,y):
    if y==1:
        return x-1
    if x==0:
        return 100000000
    if y==0:
        return 100000000
    if x==y:
        return 100000000
    return gcd(y,x%y)+int(x/y)


n = int(input())
count = n-1
for i in range(2,n):
    count = min(count,gcd(n,i))
print(count,end='')