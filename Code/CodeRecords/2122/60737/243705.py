import math


if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    print(z == 0 or (z <= x+y and z % math.gcd(x, y) == 0))
    