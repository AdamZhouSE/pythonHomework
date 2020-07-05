import math

x = int(input())
y = int(input())
z = int(input())

if z == 0:
    print(True)
else:
    print(x + y >= z and z % math.gcd(x, y) == 0)