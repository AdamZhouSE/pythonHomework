x = int(input())
y = int(input())
z = int(input())


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


if x+y>=z and z%gcd(x,y)==0:
    print(True)
else:
    print(False)