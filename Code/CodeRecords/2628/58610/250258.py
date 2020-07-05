def gcd(a: int, b: int):
    return a if b == 0 else gcd(b, a % b)

def side(a: list, b: list):
    return gcd(abs(a[0] - b[0]), abs(a[1] - b[1]))

def lattice(a: list, b: list, c: list) -> int:
    s = abs((b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])) / 2
    b = side(a, b) + side(a, c) + side(b, c)
    return int(s + 1 - b / 2)

def get_input() -> list:
    return list(map(int, input().split(' ')))

for _ in range(eval(input())):
    t = lattice(get_input(), get_input(), get_input())
    print(t)