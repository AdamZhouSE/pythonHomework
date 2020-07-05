def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
p = int(input())
q = int(input())
x = p//gcd(p,q)%2
y = q//gcd(p,q)%2
print(1 if x==y==1 else 2 if x==0 and y==1 else 0)