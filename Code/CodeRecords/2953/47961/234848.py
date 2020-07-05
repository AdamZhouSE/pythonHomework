def gcd(m,n):
  while m*n!=0:
    m=m%n
    if m==0:
        return n
    else:
        n=n%m
        if n==0:
            return m
a=int(input())
ans=a-1
for i in range(2,a):
    if ans>gcd(a,i):
        ans=gcd(a,i)
print(ans,end="")