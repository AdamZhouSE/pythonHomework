from math import gcd


def get_point():
    p = eval(input())
    q = eval(input())
    k = p * q / gcd(p, q)
    if (k / p) % 2 == 0:
        return 0
    if (k / q) % 2 == 0:
        return 2
    return 1


print(get_point())
