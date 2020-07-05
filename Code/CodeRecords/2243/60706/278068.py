p=int(input())
q=int(input())
from fractions import gcd
g = gcd(p, q)
p = (p / g) % 2
q = (q / g) % 2
if p and q:
    ans=1
else:
    if p: 
        ans=0 
    else:
        ans=2
print(ans)
