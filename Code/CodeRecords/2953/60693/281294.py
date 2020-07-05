def gcd(x,y):
    if y==1:return x-1
    if not x or not y or x==y:return float('inf')
    return gcd(y,x%y)+x//y

n=int(input())
res=n-1
for i in range(2,n):
    res=min(gcd(n,i),res)
print(res,end='')