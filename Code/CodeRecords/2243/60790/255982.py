p=int(input())
q=int(input())
from fractions import gcd
g = gcd(p, q)
p = (p / g) % 2
q = (q / g) % 2
print(1 if p and q else 0 if p else 2)