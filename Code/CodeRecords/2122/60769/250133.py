def solve(x, y, z):
    if z == 0:
        return True
    elif x + y < z:
        return False
    return z % gcd(x, y) == 0


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


a = int(input())
b = int(input())
c = int(input())
print(solve(a, b, c))
