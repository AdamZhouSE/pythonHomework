def gcd(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    if a>b:
        return gcd(a%b,b)
    else:
        return gcd(a,b%a)
a=int(input())
b=int(input())
c=int(input())
if a+b>c and c%gcd(a,b)==0:
    print("True")
else:
    print("False")
