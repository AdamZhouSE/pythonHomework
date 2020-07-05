import math
p=int(input())
q=int(input())
s=p*q/math.gcd(p,q)
if s % 2 == 1:
    if s % 2 == 1:
        print(1)
    else:
        print(2)
else:
    if s % 2 == 1:
        print(0)