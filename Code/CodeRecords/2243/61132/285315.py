def gcd(m,n):
    while n!=0:
        m,n=n,m%n
    return m



p=int(input())
q=int(input())
h=q/gcd(p,q)
s=p/gcd(p,q)
if(s%2==0):
    if(h%2==0):
        print("Error")
    else:
        print(2)
else:
    if(h%2==0):
        print(0)
    else:
        print(1)