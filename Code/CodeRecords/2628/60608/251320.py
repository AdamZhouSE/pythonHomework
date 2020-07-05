def gcd(a: int, b: int):
    return a if b == 0 else gcd(b, a % b)


def side(a: list, b: list):
    return gcd(abs(a[0] - b[0]), abs(a[1] - b[1]))


def lattice(a: list, b: list, c: list):
    s = abs((b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])) / 2
    b = side(a, b) + side(b, c) + side(a, c)
    return int(s + 1 - b / 2)


def getList():
    return list(map(int, input().split(" ")))


def func25():
    for times in range(eval(input())):
        t = lattice(getList(), getList(), getList())
        print(t)


func25()
