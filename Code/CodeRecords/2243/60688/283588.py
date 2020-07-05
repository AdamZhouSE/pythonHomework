def gcd(m,n):
    while n!=0:
        m,n=n,m%n;
    return m;
p=int(input())
q=int(input())
k=p*q;
t1=k//p
t2=k//q
res=1;
if t1&1==0:
    res=0;
if t2&1==0:
    res=2;
print(res);
