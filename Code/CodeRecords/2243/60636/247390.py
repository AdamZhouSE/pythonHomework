import math
p=int(input())
q=int(input())
s=p*q/math.gcd(p,q)
if(s%p==1):
    print(0)
else:
    if(s%q==0):
        print(2)
    else:
        print(1)