from math import gcd
def water(x,y,z):
    if z > x + y:
        return False
    if x == z or y == z or x+y == z:
        return True
    return z % gcd(x,y) == 0

x = int(input())
y = int(input())
z = int(input())
print(water(x,y,z))