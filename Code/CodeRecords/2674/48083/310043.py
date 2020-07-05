def solve():
    num = int(input())

    for _ in range(num):
        calc(input())


def calc(str):
    a = 0
    b = 0
    c = 0

    for i in str:
        if i == 'a':
            a = 2*a + 1
        elif i == 'b':
            b = a + 2*b
        elif i == 'c':
            c = b + 2*c

    print(c)


solve()