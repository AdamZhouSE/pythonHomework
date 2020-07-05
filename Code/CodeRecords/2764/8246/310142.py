def solve():
    num = int(input())

    for _ in range(num):
        n = int(input())
        res = calc(n)
        print(res)


def calc(n):
    a = int(n/2)
    b = int(n/3)
    c = int(n/4)

    if(a == 0 or b ==0 or c == 0):
        return n

    return calc(a) + calc(b) + calc(c)

solve()