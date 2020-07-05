from fractions import gcd
p = int(input())
q = int(input())
g = gcd(p, q)
p = (p / g) % 2
q = (q / g) % 2
print("1") if p and q else print("0") if p else print("2")