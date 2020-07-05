def canMeasureWater( x, y, z):
    tmp = gcd(x, y)
    if z == 0: return True
    if z > x + y: return False
    return z % tmp == 0


def gcd(x, y):
    if y == 0: return x
    return gcd(y, x % y)

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    print(canMeasureWater(x,y,z))