import math
p=int(input())
q=int(input())
s=p*q/math.gcd(p,q)
print(s)